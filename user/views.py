from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import ProfileForm


def home(request):
    user = Profile.objects.filter(user=request.user.id)
    return render(request, 'user/home.html', {user: 'user'})


# Detailview of User Profile
class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'user/profile_detail.html'
    context_object_name = 'profile'


# CreateView to create new profile
class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'user/profile_form.html'
    success_url = reverse_lazy('user:home')

    #  check if instance exists if not then creates new instance 
    def form_valid(self, form):
        instance = Profile.objects.filter(user=self.request.user).first()
        if instance:
            # Update all cleaned data fields
            for field, value in form.cleaned_data.items():
                setattr(instance, field, value)
            instance.save()
        else:
            # Create a new instance
            form.instance.user = self.request.user
            return super().form_valid(form)

       
# Updates the users profile
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'user/profile_form.html'
    
    def get_success_url(self):
        return reverse_lazy('user:profile_detail', kwargs={'pk': self.kwargs['pk']})
    
    
# Deletes user profile
class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'user/profile_delete.html'
    success_url = reverse_lazy('user:home')
    



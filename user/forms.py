from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user', 'joined_on']
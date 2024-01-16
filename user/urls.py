from django.urls import path, include
from . import views

app_name = 'user'


urlpatterns = [
    path('', views.home, name='home'), 
    path('profile/create/<int:pk>/', views.ProfileCreateView.as_view(), name='profile_create'),
    path('profile_detail/<int:pk>/', views.ProfileView.as_view(), name='profile_detail'),
    path('profile/<int:pk>/update/', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/<int:pk>/delete/', views.ProfileDeleteView.as_view(), name='profile_delete'),
]

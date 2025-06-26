from django.urls import path
from .views import RegistrationView, UserLoginView, UserLogoutView, ProfileView, ProfileEditView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', ProfileEditView.as_view(), name='edit_profile'),
]
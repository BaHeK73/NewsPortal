from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomUserCreationForm, ProfileEditForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class RegistrationView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, 'users/register.html', {'form': form})


class UserLoginView(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('profile')


class UserLogoutView(LogoutView):
    next_page = 'login'


class ProfileView(TemplateView):
    template_name = 'users/profile.html'


class ProfileEditView(LoginRequiredMixin, View):
    def get(self, request):
        form = ProfileEditForm(instance=request.user)
        return render(request, 'users/profile_edit.html', {'form': form})

    def post(self, request):
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, 'users/profile_edit.html', {'form': form})

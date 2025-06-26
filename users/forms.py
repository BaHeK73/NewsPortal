from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.forms.widgets import ClearableFileInput


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=True, label='Имя',
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите имя'})
    )
    last_name = forms.CharField(
        max_length=30, required=True, label='Фамилия',
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите фамилию'})
    )
    email = forms.EmailField(
        required=True, label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Введите email'})
    )
    avatar = forms.ImageField(
        required=True, label='Аватар',
        widget=forms.ClearableFileInput(attrs={'class': 'form-input'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Имя пользователя'})
        self.fields['password1'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Пароль'})
        self.fields['password2'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Повторите пароль'})

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'avatar')


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = 'Удалить'
    initial_text = 'Текущий файл'
    input_text = 'Изменить'


class ProfileEditForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=30, required=True, label='Имя',
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите имя'})
    )
    last_name = forms.CharField(
        max_length=30, required=True, label='Фамилия',
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите фамилию'})
    )
    email = forms.EmailField(
        required=True, label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Введите email'})
    )
    avatar = forms.ImageField(
        required=False, label='Аватар',
        widget=CustomClearableFileInput(attrs={'class': 'form-input'})
    )

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'avatar') 
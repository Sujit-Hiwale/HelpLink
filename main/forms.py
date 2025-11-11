# main/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import HelpRequest, UserProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    location = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            'first_name': 'Full Name'
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            # create linked profile
            UserProfile.objects.create(
                user=user,
                full_name=self.cleaned_data['first_name'],
                phone=self.cleaned_data.get('phone'),
                location=self.cleaned_data.get('location'),
                avatar=self.cleaned_data.get('avatar'),
            )
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Email")  # we will use email as username (username field)

class HelpRequestForm(forms.ModelForm):
    class Meta:
        model = HelpRequest
        fields = ['title', 'description', 'category']
        widgets = {
            'description': forms.Textarea(attrs={'rows':4}),
        }


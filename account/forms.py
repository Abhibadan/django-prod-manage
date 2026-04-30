from django import forms
from .models import CustomUser
from django.contrib.auth.models import Group
from django.db.models import Q

class UserRegistrationForm(forms.ModelForm):
    re_password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=[(role, role) for role in Group.objects.all()])
    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'phone_number',
            'address',
            'avatar',
            'password',
            'bio',
            'date_of_birth',
        ]

    def clean(self):
        email = self.cleaned_data.get("email")
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")
        role = self.cleaned_data.get("role")
        if not role or not Group.objects.filter(name=role).exists():
            raise forms.ValidationError("Invalid role")
        else:
            self.cleaned_data['role'] = Group.objects.get(name=role).pk
        if password != re_password:
            raise forms.ValidationError("Passwords do not match")
        elif CustomUser.objects.filter(Q(email=email) | Q(username=username)).exists():
            raise forms.ValidationError("User with this email or username already exists")
        return self.cleaned_data

class UserLoginForm(forms.ModelForm):
    """Login form for user authentication"""
    re_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'password',
        ]
    def clean(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")
        if password != re_password:
            raise forms.ValidationError("Passwords do not match")
        return self.cleaned_data
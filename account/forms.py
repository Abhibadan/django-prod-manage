from django import forms
from .models import CustomUser
from django.db.models import Q

class UserRegistrationForm(forms.ModelForm):
    re_password = forms.CharField(widget=forms.PasswordInput)
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
        if password != re_password:
            raise forms.ValidationError("Passwords do not match")
        if CustomUser.objects.filter(Q(email=email) | Q(username=username)).exists():
            raise forms.ValidationError("User with this email or username already exists")
        return self.cleaned_data

# class LoginForm(forms.Form):
#     """Login form for user authentication"""
#     class Meta:
#         model = CustomUser
#         fields = [
#             'username',
#             'password',
#             're_password',
#         ]
#     def clean(self):
#         password = self.cleaned_data.get("password")
#         re_password = self.cleaned_data.get("re_password")
#         if password != re_password:
#             raise forms.ValidationError("Passwords do not match")
#         return self.cleaned_data
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from hostels.models import HostelProfile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]


class HostelProfileForm(forms.ModelForm):
	class Meta:
		model = HostelProfile
		exclude = ['user']

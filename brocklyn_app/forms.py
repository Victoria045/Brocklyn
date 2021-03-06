from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, NeighbourHood, Business, Post

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'neighbourhood', 'profile_picture']

class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        exclude = ('admin',)


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user', 'neighbourhood')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'hood')
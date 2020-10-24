# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User,SearchHistoryModel
from django.forms import MultiWidget, TextInput
from django.forms import CheckboxInput, HiddenInput

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('email',) # new

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',) # new

class HomeForm(forms.ModelForm):
    textsearch=forms.CharField(max_length=150,required=True,
    widget=forms.TextInput( attrs={'class':'form-control',
                                   'placeholder':'What are you looking for?'}))

    class Meta:
        model=SearchHistoryModel
        fields=('textsearch',)

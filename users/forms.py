from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    bio = forms.CharField(required=True,widget=forms.Textarea(attrs={'class':'form-control','rows':3,'cols':5}))
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control'})
        self.fields['password1'].help_text = ''
        self.fields['username'].help_text = ''
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control'})
        self.fields['password2'].help_text = ''
    
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name','last_name','email','bio', 'password1', 'password2']

class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput(attrs={'class':'form-control'})
        self.fields['username'].widget = forms.TextInput(attrs={'class':'form-control'})
    
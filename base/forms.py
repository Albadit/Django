from django import forms
from .models import Book, Read, Profile, User
from django.contrib.auth.forms import UserCreationForm


class SingupForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'required': 'True',
        'class': 'form-control',
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'required': 'True',
        'class': 'form-control',
    }))
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'required': 'True',
        'class': 'form-control',
    }))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'required': 'True',
        'class': 'form-control',
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['first_name']
        user.email = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("location", "date_of_birth", "bio")
        labels = {"location": "Location", "date_of_birth": "Date of birth", "bio": "Bio"}

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("Title", "Author", "Genre", "NumberOfPages", "Approved", "Approved_by")
        labels = {"NumberOfPages": "Pages"}

class ReadForm(forms.ModelForm):
    class Meta:
        model = Read
        fields = ("Book", "User", "Score", "Date")
from django import forms
from .models import Book, Read

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
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

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("Title", "Author", "Genre", "NumberOfPages")
        widgets = {
            'Title': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Name'
            }),
            'Author': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Author'
            }),
            'Genre': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Genre'
            }),
            'NumberOfPages': forms.NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Number Of Pages'
            }),
        }

class ReadForm(forms.ModelForm):
    class Meta:
        model = Read
        fields = ("Date", "Score")
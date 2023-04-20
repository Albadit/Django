from django import forms
from .models import Book, Read, Profile

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

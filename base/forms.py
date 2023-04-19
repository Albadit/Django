from django import forms
from .models import Book, Read

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("Title", "Author", "Genre", "NumberOfPages")

class ReadForm(forms.ModelForm):
    class Meta:
        model = Read
        fields = ("Date", "Score")
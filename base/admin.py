from django.contrib import admin
from .models import Book, Read, Profile

# # Register your models here.
admin.site.register(Profile)
admin.site.register(Book)
admin.site.register(Read)
from django.contrib import admin
from .models import Profile, Read, Book

# Register your models here.
admin.site.register(Profile)
admin.site.register(Read)
admin.site.register(Book)
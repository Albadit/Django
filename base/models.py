from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
class Profile(models.Model):
    location = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
    
class Book(models.Model):
    Title = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    Genre = models.CharField(max_length=100)
    NumberOfPages = models.CharField(max_length=100)
    Approved = models.BooleanField(default=False)
    Approved_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='approved_by', null=True, blank=True)
    def __str__(self):
        return self.Title
    
class Read(models.Model):
    Book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="approved_by")
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Date = models.DateField(null=False, blank=False)
    Score = models.IntegerField(null=False, blank=False)
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
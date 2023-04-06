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

    def __str__(self) -> str:
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

class Distance(models.Model):
    length = models.CharField(max_length=30, blank=True)
    full_name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.length

class Time(models.Model):
    distance = models.ForeignKey(Distance, on_delete=models.CASCADE, null=False)
    time_in_minutes = models.IntegerField(blank=False,)
    date = models.DateField(blank=False,)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='approved_by', null=True, blank=True)

    def __str__(self):
        return f"{self.distance.length} by {self.user.get_username()}"

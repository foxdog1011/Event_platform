from django.db import models
from django.contrib.auth.models import User
from events.models import Event


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username} 的個人資料'


from django.db import models
from django.contrib.auth.models import User
from events.models import Event


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    # 可以添加更多字段，如头像、联系方式等

    def __str__(self):
        return f'{self.user.username} 的个人资料'


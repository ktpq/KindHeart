from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # เพิ่ม field ของคุณเอง
    class SystemRole(models.TextChoices):
        ADMIN = "admin"
        USER = "user"
    role = models.CharField(
        max_length=6, 
        choices=SystemRole.choices, 
        default=SystemRole.USER
    )

    class UserStatus(models.TextChoices):
        NORMAL = "normal"
        BANNED = "banned"
    status = models.CharField(
        max_length=7, 
        choices=UserStatus.choices, 
        default=UserStatus.NORMAL
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username








    
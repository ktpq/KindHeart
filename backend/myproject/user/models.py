from django.db import models

# Create your models here.
class User (models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=150)

    class SystemRole(models.TextChoices):
        ADMIN = "admin"
        USER = "user"
    role = models.CharField(max_length=6, choices=SystemRole.choices, default=SystemRole.USER)

    class UserStatus(models.TextChoices):
        NORMAL = "normal"
        BANNED = "banned"
    
    status = models.CharField(max_length=7, choices=UserStatus.choices, default=UserStatus.NORMAL)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)







    
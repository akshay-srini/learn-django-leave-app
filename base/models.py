from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CompanyUser(AbstractUser):
    position = models.CharField(max_length=150)

    def __str__(self):
         return f"{self.user.username} - {self.position}"
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CompanyUser(AbstractUser):
    position_choices = [
        ('employee', 'employee'),
        ('manager', 'manager')
    ]
    position = models.CharField(max_length=100, choices=position_choices, default='employee')

    def __str__(self):
        return f"{self.username} - {self.position}"

class Leaves(models.Model):
    leave_type_choices = [
        ('casual', 'casual'),
        ('sick', 'sick')
    ]
    leave_status_choices = [
        ('pending', 'pending'),
        ('successful', 'successful'),
        ('rejected', 'rejected')
    ]
    employee = models.ForeignKey(CompanyUser, on_delete=models.CASCADE)
    no_of_days = models.IntegerField(default=0, null=False)
    leave_type = models.CharField(choices=leave_type_choices, default='casual', max_length=100)
    reason = models.CharField(blank=True, null=True, max_length=500)
    status = models.CharField(choices=leave_type_choices, default='pending', max_length=100)

    def __str__(self):
        return super().__str__()
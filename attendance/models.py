"""import statements"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from datetime import datetime, timezone #python builtin timezone class
from django.utils import timezone #django timezone helper module
# Create your models here.

#validation for nepali phone numbers
nepali_phone_regex = RegexValidator(
    regex=r'^9[6-8]\d{8}$',
    message=_("Kindly enter valid phone numbers")
)

def make_aware_if_naive(dt):
    if dt is None:
        return None
    if timezone.is_naive(dt):
        return timezone.make_aware(dt)
    return dt

class Department(models.Model):
    name = models.CharField(max_length=255, unique = True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)#this cannot be changed when the object is changed later
    updated_at = models.DateTimeField(auto_now=True)
    work_start_time = models.TimeField(defailt="09:00")
    work_end_time = models.TimeField(default = "17:00")
    working_days_per_week = models.IntegerField(default=6)
    
    def __str__(self):
        return self.name

class User(AbstractUser):
    email=models.EmailField(unique=True)
    USERNAME_FIELD = "email" #TODO: to set in settings.py to use email as username
    REQUIRED_FIELDS = ['username']
    def __str__(self):
        return self.email
    is_verified = models.BooleanField(default=False)
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)

class Employee(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    EMPLOYMENT_TYPE = [
        ('FULL_TIME', 'Full Time'),
        ('PART_TIME', 'Part Time'),
        ('CONTRACT', 'Contract'),
        ('INTERN', 'Intern')
    ]
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('MANAGER', 'Manager'),
        ('HR', 'Hr'),
        ('EMPLOYEE', 'Employee')
    ]
    user=models.OneToOneField(User, on_delete=models.CASCADE, db_index=True, related_name='Employee_profile')
    role=models.CharField(max_length=20, choices=ROLE_CHOICES, default='EMPLOYEE', db_index=True)
    phone=models.CharField(_('Phone'), max_length=10, validators=[nepali_phone_regex], db_index=True)
    gender=models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(null=False,blank=False)
    department=models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
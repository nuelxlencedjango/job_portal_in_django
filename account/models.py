from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    email =models.EmailField(unique=True)
    is_recruiter =models.BooleanField(default=False)
    is_applicant =models.BooleanField(default=False)
    is_resume =models.BooleanField(default=False)
    is_company =models.BooleanField(default=False)

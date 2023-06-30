from django.db import models
from account.models import User


#from artisan.models import Artisan

class Employers(models.Model):

   user = models.OneToOneField(User, on_delete=models.CASCADE)
   name = models.CharField(max_length=200)
   location = models.CharField(max_length=200)
   state = models.CharField(max_length=200)
   #job_title = models.CharField(max_length=200)
   establisedDate = models.DateField(auto_now_add = True, null=True, blank=True)
   date_created = models.DateField(auto_now_add = True, null=True, blank=True)
   class Meta:
      verbose_name_plural='Employers'
       
      ordering = ['-date_created']

   def __str__(self):
      return f"{self.name}-{self.user} - {self.location}"

     

  
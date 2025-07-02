from django.db import models
from  django.contrib.auth.models import User

class user(models.Model):
    user_name=models.CharField(max_length=50)
    user_mail=models.CharField(max_length=50)
    user_number=models.IntegerField(null=True, blank=True)

    def __str__(self):
            return f"{self.user_name}, {self.user_mail}, {self.user_number}"
    
        

    

# Create your models here.

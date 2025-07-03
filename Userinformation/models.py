from django.db import models
from  django.contrib.auth.models import User
import uuid
from safedelete.models import SafeDeleteModel




class user(SafeDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name=models.CharField(max_length=50)
    user_mail=models.EmailField(max_length=50)
    user_number=models.BigIntegerField(null=True, blank=True,max_length=10)
    
    def __str__(self):
            return f"{self.user_name}, {self.user_mail}, {self.user_number}"
    
        

    # edit-
    # emailfield-
    # softdelete or safedelete
    # uuid-
    # app url-
    # class based views

# Create your models here.

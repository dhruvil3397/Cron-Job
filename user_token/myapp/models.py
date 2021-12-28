from django.db import models
from django.contrib.auth.models import User

# Create your models here.
choice = (('Admin','Admin'),
            ('Editor','Editor'),
            ('Uploader','Uploader'))

class UserProfile(models.Model):
    user = models.OneToOneField(User,related_name='profile', on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10,blank=True,null=True)
    permission = models.CharField(max_length=100,choices= choice)

    def __str__(self) -> str:
        return self.user.username
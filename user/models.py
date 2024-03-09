from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Userprofileinfo(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)

    profileimage=models.ImageField(upload_to="profile_pics",blank=True)
    portfolio=models.URLField(blank=True)



    def __str__(self):
        return self.user.username
    

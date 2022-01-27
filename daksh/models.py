from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , primary_key=True )
    name = models.CharField(max_length=35)
    branch = models.CharField(max_length=60)
    reg_no = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=25)
    session = models.CharField(max_length=35)
    image = models.ImageField(upload_to = 'users' , default = "")
    about = models.CharField(max_length=200 , default = "")


    def __str__(self):
        return self.name
    
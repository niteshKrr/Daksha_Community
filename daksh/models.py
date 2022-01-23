from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=35)
    branch = models.CharField(max_length=60)
    reg_no = models.IntegerField(40)
    roll_no = models.CharField(max_length=20)
    session = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'users' , default = "")

    def __str__(self):
        return self.name
    
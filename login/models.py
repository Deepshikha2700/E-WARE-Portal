from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# from tinymce import models as tinymce_models
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email= models.EmailField()
    phone= models.CharField(max_length=10)
    message=models.TextField()
    def __str__(self):
        return self.name

class Profile(models.Model):
    #user_id=models.OneToOneField(User,blank=True,null=True,on_delete=models.CASCADE)
    fullName = models.CharField(max_length=50)
    eMail = models.EmailField()
    phone = models.IntegerField()
    gender = models.CharField(max_length=10,null=True,blank=True)
    Street = models.CharField(max_length=50,null=True,blank=True)
    ciTy = models.CharField(max_length=100,null=True,blank=True)
    sTate = models.CharField(max_length=50,null=True,blank=True)
    zIp = models.CharField(max_length=30,null=True,blank=True)
    site=models.CharField(max_length=30,null=True,blank=True)
    FaceBook= models.CharField(max_length=30,null=True,blank=True)
    Organization_Name = models.CharField(max_length=30,null=True,blank=True)
    Job_Title = models.CharField(max_length=30,null=True,blank=True)
    added_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.fullName


# class User(models.Model):
#     username=models.EmailField()
#     password=models.CharField(max_length=20)


#form models
class Phishing(models.Model):
    # OPTIONS = (
    #     ('D_D.html', 'Devices and Data Security'),
    #     # ('saab’,’Saab’),
    #     # ('fiat’,’Fiat’), 
    #     # ('audi’,’Audi’), 
    #     )
    # Form_id=models.AutoField(unique=True,default=1)

    #user=models.OneToOneField(User,null=True,on_delete=models.CASCADE,)
    # user=models.OneToOneField(User,on_delete=models.CASCADE)


    name=models.CharField(max_length=100)
    Select_Template_Category=models.CharField(max_length=100,null=True)
    select_country=models.CharField(max_length=100,null=True)
    mail=models.EmailField()
    sname=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    # date=models.DateTimeField(blank=True,null=True)
    myfile=models.FileField(upload_to="")
    count=models.CharField(max_length=100)
    interval=models.CharField(max_length=100)
    ttype=models.CharField(max_length=100)
    # name=models.CharField(max_length=100)
    # name=models.CharField(max_length=100)
    # name=models.CharField(max_length=100)
    # name=models.CharField(max_length=100)
    # name=models.CharField(max_length=100)
    # name=models.CharField(max_length=100)
    # name=models.CharField(max_length=100)
    # name=models.CharField(max_length=100)
    def __str__(self):

        return self.Select_Template_Category
#signup model


# class Template_Category(models.Model):
#     Select_Template_Category=models.CharField(max_length=100)
class Date_user(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    dob=models.DateField(default=True,null=True)

    def __str__(self):
        return self.user.username
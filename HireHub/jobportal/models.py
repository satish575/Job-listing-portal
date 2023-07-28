from django.db import models

# Create your models here.

class User(models.Model):
    firstname = models.CharField(max_length=30, default='')
    lastname = models.CharField(max_length=150, default='')
    username = models.CharField(max_length=150, unique=True, null=False, blank=False)
    email=models.EmailField(default='')
    password=models.CharField(max_length=20,default='')
    
    
    def __str__(self):
        return self.firstname

class Jobs(models.Model):
    jobTitle=models.CharField(max_length=50,default="")
    jobDescription=models.CharField(max_length=1000,default="")
    jobRequirement=models.CharField(max_length=1000,default="")
    companyName=models.CharField(max_length=50,default="")
    
    def __str__(self) -> str:
        return super().__str__()

class Applications(models.Model):
    fullname=models.CharField(max_length=20,null=False, blank=False)
    username=models.CharField(max_length=20,null=False, blank=False)
    email=models.CharField(max_length=50,null=False, blank=False)
    query=models.CharField(max_length=1000,null=False, blank=False)
    cv=models.FileField(upload_to="cv/",max_length=250,null=True,default=None)
    jobid=models.IntegerField(default=-1 ,null=False,blank=False)
    
    def __str__(self) -> str:
        return super().__str__()

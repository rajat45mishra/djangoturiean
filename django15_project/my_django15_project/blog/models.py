from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class addasset(models.Model):
    Assettype = models.CharField(max_length=50)
    Assetsequence = models.CharField(max_length=50)
    Assetname = models.CharField(max_length=50)
    Assetnumber = models.CharField(max_length=50)
    DateofPurchase = models.DateField()
    AssestWarrentyUpto = models.DateField()


    def __str__(self):
        return self.title

class ProjectDetail(models.Model):
    ProjectNumber = models.CharField(max_length=50)
    ProjectName = models.CharField(max_length=50)
    ProjectContact = models.CharField(max_length=50)
    ProjectAddress = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class AddProjectDocument(models.Model):
    DocumentType = models.CharField(max_length=50)
    DocumentSequence = models.CharField(max_length=50)
    DocumentNumber = models.CharField(max_length=50)
    DocumentName = models.CharField(max_length=50)
    Attachment = models.FileField(upload_to='documents/')


    def __str__(self):
        return self.title

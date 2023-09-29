from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=120)
    content=models.TextField()  
    timestamp=models.DateTimeField(null=True,auto_now_add=True)
    updated=models.DateField(null=True,auto_now=True)
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=120)
    slug=models.SlugField(null=True,blank=True)
    content=models.TextField()  
    timestamp=models.DateTimeField(null=True,auto_now_add=True)
    updated=models.DateField(null=True,auto_now=True)
    publish=models.DateTimeField(auto_now_add=False,auto_now=False,default=timezone.now)  

    def save(*args, **kwargs):
        super().save(*args, **kwargs)
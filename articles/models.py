from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save,post_save
from django.urls import reverse
import random
from .utils import slugify_instance_title

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=120)
    slug=models.SlugField(unique=True, null=True,blank=True)
    content=models.TextField()  
    timestamp=models.DateTimeField(null=True,auto_now_add=True)
    updated=models.DateField(null=True,auto_now=True)
    publish=models.DateTimeField(auto_now_add=False,auto_now=False,default=timezone.now) 

    def get_absolute_url(self):
         return reverse("article-detail",kwargs={"slug":self.slug})

    def save(self,*args, **kwargs):
        # if self.slug is None:
        #     self.slug=slugify(self.title)
        super().save(*args, **kwargs)

# def slugify_instance_title(instance,save=False,new_slug=None):
#     if new_slug is not None:
#          slug=new_slug
#     else:
         
#         slug=slugify(instance.title)
#     Klass=instance.__class__
#     qs=Klass.objects.filter(slug=slug).exclude(id=instance.id)
#     if qs.exists():
#          randNumber=random.randint(300_000, 500_000)
#          slug=f"{slug}-{randNumber}"
#          return slugify_instance_title(instance,save=False,new_slug=slug)
#     instance.slug=slug
#     if save:
#         instance.save()
#     return instance
    

def article_pre_save(sender,instance,*args, **kwargs):
    # print("pre_save")
    if instance.slug is None:
            slugify_instance_title(instance)
   

pre_save.connect(article_pre_save,sender=Article)


def article_post_save(sender,instance,created,*args, **kwargs):
    # print("post_save")
    print(args,kwargs)
    if created:
         slugify_instance_title(instance, save=True)

post_save.connect(article_post_save,sender=Article)
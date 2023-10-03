from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save,post_save

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=120)
    slug=models.SlugField(null=True,blank=True)
    content=models.TextField()  
    timestamp=models.DateTimeField(null=True,auto_now_add=True)
    updated=models.DateField(null=True,auto_now=True)
    publish=models.DateTimeField(auto_now_add=False,auto_now=False,default=timezone.now)  

    def save(self,*args, **kwargs):
        # if self.slug is None:
        #     self.slug=slugify(self.title)
        super().save(*args, **kwargs)

def slugify_instance_title(instance,save=False):
    slug=slugify(instance.title)
    instance.slug=slug
    if save:
        instance.save()
    return instance
    

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
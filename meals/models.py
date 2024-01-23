
from django.db import models
from django.conf import settings
from recipes.models import Recipe

# Create your models here.


User=settings.AUTH_USER_MODEL


class MealStatus(models.TextChoices):
    PENDING='p','Pending'
    COMPLETED='c','Completed'
    EXPIRED='e','Expired'
    ABORTED='a','Aborted'



class MealQuerySet(models.QuerySet):
     def by_user_id(self,user_id):
         return self.filter(user_id=user_id)
     
     def by_user(self,user):
         return self.filter(user=user)
     
     def pending(self):
         return self.filter(status=MealStatus.PENDING)
     
     def completed(self):
         return self.filter(status=MealStatus.COMPLETED)
     
     def expired(self):
         return self.filter(status=MealStatus.EXPIRED)
     
     def aborted(self):
         return self.filter(status=MealStatus.ABORTED)
    
     def in_queue(self,recipe_id):
         return self.pending().filter(recipe_id=recipe_id).exists()
    

          
class MealManager(models.Manager):
     def get_queryset(self):
          return MealQuerySet(self.model, using=self._db)
     
     def by_user_id(self,user_id):
         return self.get_queryset().by_user_id(user_id=user_id)
     
     def by_user(self,user):
         return self.get_queryset().by_user(user)
     
     def get_queue(self,user,prefetch_ingredient=False):
         qs=self.get_queryset().by_user(user).pending()
         if prefetch_ingredient:
             return qs.prefetch_related("recipe__recipeingredient")
         return qs
         
     
     def toggle_in_queue(self, user_id,recipe_id):
         qs=self.get_queryset().all().by_user_id(user_id)
         already_queued=qs.in_queue(recipe_id)
         added=None
         if already_queued:
             recipe_qs=qs.filter(recipe_id=recipe_id)
             recipe_qs.update(status=MealStatus.ABORTED)
             added=False
         else:
             obj=self.model(
                 user_id=user_id,
                 recipe_id=recipe_id,
                 status=MealStatus.PENDING

             )
             obj.save()
             added=True
         return added



         
    

class Meal(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE)
    directions=models.TextField(blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    status=models.CharField(max_length=1, choices=MealStatus.choices,default=MealStatus.PENDING)

    objects=MealManager()
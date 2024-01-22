from django.contrib.auth import get_user_model
from meals.models import Meal
from django.db.models import Sum
from recipes.models import RecipeIngredient

User=get_user_model()
j=User.objects.first()

j.meal_set.all().pending() 
queue=Meal.objects.by_user(j).pending().prefetch_related('recipe__recipeingredient')
ids=queue.values_list("recipe__recipeingredient__id", flat=True)
 
qs=RecipeIngredient.objects.filter(id__in=ids) 

data=qs.values("name","unit").annotate(total=Sum("quantity_as_float"))

for d in data:
    print(d)






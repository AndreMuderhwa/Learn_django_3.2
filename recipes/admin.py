from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Recipe,RecipeIngredient,RecipeIngredientImage
# Register your models here.

#TabularInline,StackedInline => sont des types d'affichages
User=get_user_model()

# admin.site.unregister(User)

# class RecipeInline(admin.StackedInline):
#     model=Recipe
#     extra=0
#     # fields=['name','quantity','unit','directions']




# class UserAdmin(admin.ModelAdmin):
#     inlines=[RecipeInline]
#     list_display=['username']

# admin.site.register(User,UserAdmin)

class RecipeIngredientInline(admin.StackedInline):
    model=RecipeIngredient
    extra=0
    # fields=['name','quantity','unit','directions']
    readonly_fields=['quantity_as_float','as_mks','as_imperial'] #we can add 'to_ounces' if we want to make the conversion

class RecipeAdmin(admin.ModelAdmin):
    inlines=[RecipeIngredientInline]
    list_display=['name','user']
    readonly_fields=['timestamp','updated']
    raw_id_fields=['user']

admin.site.register(Recipe,RecipeAdmin)
admin.site.register(RecipeIngredient)
admin.site.register(RecipeIngredientImage)
# Generated by Django 3.2.5 on 2024-01-20 06:50

from django.db import migrations, models
import recipes.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_recipeingredientimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredientimage',
            name='image',
            field=models.ImageField(upload_to=recipes.models.recipe_ingredient_image_upload_handler),
        ),
    ]
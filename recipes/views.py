from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from django.urls import reverse
from .models import Recipe,RecipeIngredient
from .forms import RecipeForm,RecipeIngredientForm

# Create your views here.
@login_required
def recipe_list_view(request):
    qs=Recipe.objects.filter(user=request.user)
    context={
        "object_list":qs
    }
    return render(request,"recipes/list.html",context)

@login_required
def recipe_detail_view(request,id=None):
    hx_url= reverse("recipes:hx-detail", kwargs={"id": id})
    context={
        "hx_url":hx_url
    }
    return render(request,"recipes/detail.html",context)



@login_required
def recipe_detail_hx_view(request,id=None):
    if not request.htmx:
        raise Http404
    
    try:
        obj=Recipe.objects.get(id=id,user=request.user)
    except:
        obj=None
    if obj is None:
        return HttpResponse("Not Found")
    context={
        "object":obj
    }
    return render(request,"recipes/partials/detail.html",context)





@login_required
def recipe_create_view(request,id=None):
    form=RecipeForm(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        obj=form.save(commit=False)
        obj.user=request.user
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request,"recipes/create-update.html",context)

@login_required
def recipe_update_view(request,id=None):
    obj=get_object_or_404(Recipe,id=id,user=request.user)
    form=RecipeForm(request.POST or None,instance=obj)

    context={
        "form":form,
        "object":obj
    }
    if form.is_valid():
        form.save()
        context['message']="Data Saved."
        
    if request.htmx:
        return render(request,"recipes/partials/forms.html",context)
    return render(request,"recipes/create-update.html",context)


@login_required
def recipe_ingredient_detail_hx_view(request,paren_id=None,id=None):
    if not request.htmx:
        raise Http404 
    try:
        parent_obj=Recipe.objects.get(id=paren_id,user=request.user)
    except:
        obj=None
    if obj is None:
        return HttpResponse("Not Found")
    instance=None
    if id is not None:
        try:
            instance=RecipeIngredient.objects.get(recipe=parent_obj,id=id)
        except:
            instance=None
    form=RecipeIngredientForm(request.POST or None, instance=instance)
    context={
        "form":form,
        "object":instance
    }
    if form.is_valid():
        new_obj=form.save(commit=False)
        if instance is None:
            new_obj.recipe=parent_obj
        new_obj.save()
        context['object']=context
        return render(request,"recipes/partials/ingredient-inline.html",context)

    return render(request,"recipes/partials/ingredient-form.html",context)
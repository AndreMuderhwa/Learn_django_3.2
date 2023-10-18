from django.shortcuts import render
from . models import Article
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.db.models import Q
from . forms import ArticleForm
# Create your views here.

def article_detail_view(request,slug=None):
    article_obj=None
    if slug is not None:
        try:
            article_obj=Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            raise Http404
        except:
            raise Http404
    
    context={
        "object":article_obj
    }
    return render(request,"articles/detail.html",context=context)

def article_search_view(request):
    query=request.GET.get('q')
    # qs=Article.objects.all()
    # article_obj=None
    # if query is not None:
    #     lookups=Q(title__icontains=query) | Q(content__icontains=query)
        # qs=Article.objects.filter(lookups)
    qs=Article.objects.filter(title__icontains='t').search(query=query)
    context={
        "object_list":qs
    }
    return render(request,"articles/search.html",context=context)

@login_required
def article_create_view(request):
    form=ArticleForm(request.POST or None)
    context={
        "form":form
        }
    if form.is_valid():
        article_obj=form.save()
        context['form']=ArticleForm()
        # title=form.cleaned_data.get("title")
        # content=form.cleaned_data.get("content")
        # article_obj=Article.objects.create(title=title,content=content)
        # context['object']=article_obj
        # context['created']=True 
    return render(request,"articles/create.html",context=context)



# def article_create_view(request):
#     form=ArticleForm()
#     context={
#         "form":form
#         }
#     if request.method=="POST":
#         form=ArticleForm(request.POST)
#         context['form']=form
#         if form.is_valid():
#             title=form.cleaned_data.get("title")
#             content=form.cleaned_data.get("content")
#             article_obj=Article.objects.create(title=title,content=content)
#             context['object']=article_obj
#             context['created']=True 
#         # title=request.POST.get("title")
#         # content=request.POST.get("content")
#         # article_obj=Article.objects.create(title=title,content=content)
#         # context['object']=article_obj
#         # context['created']=True 
#     return render(request,"articles/create.html",context=context)
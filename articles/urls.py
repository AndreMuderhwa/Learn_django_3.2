
from django.urls import path,include

from articles.views import(
    article_create_view,
    article_search_view,
    article_detail_view
) 


app_name="articles"

urlpatterns = [

    path('',article_search_view,name="search"),
    path('create/',article_create_view, name="create"),
    path('<slug:slug>/',article_detail_view,name="detail"),
       
]
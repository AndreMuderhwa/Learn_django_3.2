"""

retourner html 
"""
import random
from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string,get_template


nom="Andrew"
number=random.randint(10,120098978876)
article_obj=Article.objects.get(id=2)
article_title=article_obj.title
article_content=article_obj.content
article_queryset=Article.objects.all()


context={
    "object_list":article_queryset,
    "object":article_obj,
    "id":article_obj.id,
    "title":article_obj.title,
    "content":article_obj.content
}


tmp =get_template("home-view.html")
tmpl_string=tmp.render(context=context)

HTML_STRING=render_to_string("home-view.html",context=context)
# HTML_STRING="""
#     <h1>{title}  (id :{id})!</h1>

#      <p>   {content}   </p>
# """.format(**context)

def home_view(request,*args,**kwargs):

    
    return HttpResponse(HTML_STRING)
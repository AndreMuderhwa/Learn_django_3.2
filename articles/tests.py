from django.test import TestCase
from .models import Article
from django.utils.text import slugify
from .utils import slugify_instance_title
# Create your tests here.

class ArticleTestCase(TestCase):
    def setUp(self):
        self.number_of_article=5
        for i in range(0, self.number_of_article):
            Article.objects.create(title='Hello world',content='something else')

    def test_queryset_exists(self):
        qs=Article.objects.all()
        self.assertTrue(qs.exists())
    
    def test_queryset_count(self):
        qs=Article.objects.all()
        self.assertEqual(qs.count(), self.number_of_article)
    
    def test_hello_world_slug(self):
        obj=Article.objects.all().order_by("id").first()
        title=obj.title
        slug=obj.slug
        slugified_title=slugify(title)
        self.assertEqual(slug,slugified_title)

    def test_hello_world_unique_slug(self):
        qs=Article.objects.exclude(slug__iexact='hello-world')
        for obj in qs:
            title=obj.title
            slug=obj.slug
            slugified_title=slugify(title)
            self.assertEqual(slug,slugified_title)

    def test_slugify_instance_title(self):
        obj=Article.objects.all().last()
        new_slugs=[]
        for i in range(0,5):
            instance=slugify_instance_title(obj, save=False)
            new_slugs.append(instance.slug)
        unique_slug=list(set(new_slugs))
        self.assertEqual(len(new_slugs),len(unique_slug))
    
    def test_slugify_instance_title_redux(self):
        slug_list=Article.objects.all().values_list('slug',flat=True)
        unique_slug_list=list(set(slug_list))
        self.assertEqual(len(slug_list),len(unique_slug_list))




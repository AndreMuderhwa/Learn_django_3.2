from django.test import TestCase
from .models import Article
from django.utils.text import slugify
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



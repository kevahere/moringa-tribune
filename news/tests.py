import datetime as dt
from django.test import TestCase
from .models import Editor,Article,tags

# Create your tests here.
class EditorTestClass(TestCase):

    #Set up method
    def setUp(self):
        self.kevin = Editor(first_name='Kevin', last_name ='Ahere',email = 'kevahere@gmail.com')

#Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kevin,Editor))
#Testing save method

    def test_save_method(self):
        self.kevin.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

    #Testing deletion
    def test_delete_method(self):
        self.kevin.save_editor()
        self.kevin.delete_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) == 0)

#Tests for Articles
class ArticleTestClass(TestCase):
    def setUp(self):
        #creating a new editor and saving it
        self.kevin = Editor(first_name='Kevin', last_name ='Ahere',email = 'kevahere@gmail.com')
        self.kevin.save_editor()

        #Creating a new tag and saving it
        self.new_tag = tags(name ='testing')
        self.new_tag.save()

        #Creating a new article and saving it
        self.new_article=Article(title ='TestArticle', post = 'This is a random test post', editor = self.kevin)
        self.new_article.save()
        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)
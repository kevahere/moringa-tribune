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

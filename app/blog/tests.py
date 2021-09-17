from django.contrib.auth.models import User
from django.test import TestCase
from blog.models import Post

class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('localhost:8000')
        self.assertEqual(response.status_code, 404)

# class PostTests(TestCase):

#     def setUp(self):
#         Post.objects.create(title='just a title',author=None)

#     def test_text_content(self):
#         post = Post.objects.get(author_id=1)
#         expected_object_name = f'{post.title}'
#         self.assertEquals(expected_object_name, 'just a title')

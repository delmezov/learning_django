from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User

from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username='username1', password='abc123'
        )
        testuser1.save()

        # Create a blog post
        test_post1 = Post.objects.create(
            author=testuser1, title='Blog title', body='Body content...'
        )
        test_post1.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'

        self.assertEquals(author, 'username1')
        self.assertEquals(title, 'Blog title')
        self.assertEquals(body, 'Body content...')

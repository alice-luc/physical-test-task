from django.test import TestCase
from thread.models import Post


class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(title="test", text="text")

    def test_post(self):
        """Пост создается и число просмотров увеличивается"""
        test_post = Post.objects.get(title="test")
        test_post.increase_num_of_views()

        self.assertEqual(str(test_post), 'test')
        self.assertEqual(test_post.number_of_views, 1)

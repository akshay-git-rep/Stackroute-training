from unittest import TestCase
from post import Post

class TestPost(TestCase):
 
    def test_create_post(self):
        p = Post("title1", "content1")
        self.assertEqual("title1", p.title)
        self.assertEqual("content1", p.content)
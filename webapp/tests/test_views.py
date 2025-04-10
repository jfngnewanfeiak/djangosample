from django.test import TestCase
from django.urls import reverse
from webapp.models import Post
  
    

class PostListTests(TestCase):
    def setUp(self):
        post1 = Post.objects.create(title="title1", text="text1")
        post2 = Post.objects.create(title="title2", text="text2")

    
    def test_get(self):
        response = self.client.get(reverse("webapp:post_list"))
        self.assertEqual(response.status_code, 200)

    def test_get_2posts_by_list(self):
        responce = self.client.get(reverse("webapp:post_list"))
        self.assertEqual(responce.status_code, 200)
        self.assertQuerysetEqual(
            responce.context['post_list'],
            ['<Post: title1>', '<Post: title2>'],
            ordered=False
        )
        self.assertContains(responce, 'title1')
        self.assertContains(responce, "title2")

    
    def tearDown(self):
        post1 = Post.objects.create(title="title1",text="text1")
        post2 = Post.objects.create(title="title2", text="text2")

class PostCreateTests(TestCase):
    def test_get(self):
        response = self.client.get(reverse('webapp:post_create'))
        self.assertEqual(response.status_code, 200)

    def test_post_with_data(self):
        data = {
            'title': 'test_title',
            'text': 'test_text'
        }
        response = self.client.post(reverse('webapp:post_create'),data=data)
        self.assertEqual(response.status_code,302)

    def test_post_null(self):
        data = {}
        response = self.client.post(reverse('webapp:post_create'),data=data)
        self.assertEqual(response.status_code, 200)

class PostDetailTests(TestCase):
    def test_not_found_pk_get(self):
        response = self.client.get(
            reverse('webapp:post_detail', kwargs={'pk': 1}),
        )
        self.assertEqual(response.status_code, 404)

    def test_get(self):
        post = Post.objects.create(title='test_title', text='test_text')
        response = self.client.get(
            reverse('webapp:post_detail', kwargs={'pk': post.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post.title)
        self.assertContains(response, post.text)


class PostUpdateTests(TestCase):
    def test_not_found_pk_get(self):
        response = self.client.get(
            reverse('webapp:post_update', kwargs={'pk':1}),
        )
        self.assertEqual(response.status_code, 404)
    
    def test_get(self):
        post = Post.objects.create(title='test_title',text='test_text')
        response = self.client.get(
            reverse('webapp:post_delete', kwargs={'pk': post.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post.title)
        self.assertContains(response, post.text)
    
class PostDeleteTests(TestCase):

    def test_not_found_pk_get(self):
        response = self.client.get(
            reverse('webapp:post_delete',kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 404)
    
    def test_get(self):
        post = Post.objects.create(title="test_title",text="test_text")
        response = self.client.get(
            reverse('webapp:post_delete', kwargs={'pk':post.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post.title)
        self.assertContains(response, post.text)

from django.urls import reverse
from django.test import TestCase
from .models import post, category
from django.contrib.auth.models import User
from .forms import postform

class TestViews(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser', password='Bgokul92@')  # Create a test user
        self.category = category.objects.create(name='Test Category')  # Create a test category
        self.post = post.objects.create(
            title='Test Post',
            title_tag='Test Tag',
            author=self.user,
            category=self.category,
            body='Test body'
        )  # Create a test post

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_article_detail_view(self):
        response = self.client.get(reverse('article_detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articledetail.html')

    # Add more test cases for other views as needed

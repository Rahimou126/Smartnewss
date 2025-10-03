

from django.test import TestCase
from django.urls import reverse
from .models import News
from django.utils import timezone

class NewsListViewTests(TestCase):

    
    def test_news_list_status_code(self):
        
        url = reverse('fetch')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_news_list_template_used(self):
        
        url = reverse('fetch')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'listofnews.html')

    

    def test_news_list_order(self):
        
        url = reverse('fetch')
        response = self.client.get(url)
        news_list = response.context['listofnews']
        self.assertGreaterEqual(news_list[0].created_at, news_list[1].created_at)




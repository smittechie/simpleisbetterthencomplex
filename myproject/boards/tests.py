from django.test import TestCase
from django.urls import reverse
from .views import home , board_topics
from.views import Board
from django.urls import resolve

# Create your tests here.
class HomeTests(TestCase):
    def test_home_view_test_case(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEquals(response.status_code ,200)

    def test_home_url_test_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func,home)


class BoardTopicsTest(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')

    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics',kwargs = {'pk':1})
        response = self.client.get(url)
        self.assertEquals(response.status_code,200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics',kwargs ={'pk':99})
        response= self.client.get(url)
        self.assertEquals(response.status_code,404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func,board_topics)
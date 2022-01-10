from django.test import TestCase
from .models import *

class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='Vikki', password='testing@123')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()

class TestNeighbourHood(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='Vikki')
        self.neighborhood = NeighbourHood(id=1, name='Gigiri', location='Nairobi',hood_logo='images/img1.jpg',description='desc',health_tell='722222222', police_number='7100000000')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_neighbourhood(self):
        self.user.save()

    def test_delete_neighbourhood(self):
        self.user.delete()

class TestBusiness(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='Vikki')
        self.business = Business.objects.create(id=1, name='Hotel', email='hotel@info.co.ke', description='desc')

    def test_instance(self):
        self.assertTrue(isinstance(self.business, Business))

    def test_save_business(self):
        self.business.save_business()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)

    def test_get_businesses(self):
        self.business.save()
        businesses = Business.all_businesss()
        self.assertTrue(len(businesses) > 0)

    def test_delete_business(self):
        self.post.delete_business()
        business = Business.search_project('test')
        self.assertTrue(len(business) < 1)

class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='Vikki')
        self.post = Post.objects.create(id=1, title='test post', post='desc')

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save_post(self):
        self.post.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0)

    def test_get_posts(self):
        self.post.save()
        posts = Post.all_posts()
        self.assertTrue(len(posts) > 0)

    def test_delete_post(self):
        self.post.delete_post()
        post = Post.search_project('test')
        self.assertTrue(len(post) < 1)
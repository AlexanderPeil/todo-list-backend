from django.test import Client
from django.test import TestCase
import unittest
from django.contrib.auth.models import User
from django.test import Client



class URLTests(TestCase):
    def test_testhomepage(self):
        response = self.client.get('/chat/')
        self.assertEqual(response.status_code, 200)

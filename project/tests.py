from django.test import TestCase
from rest_framework.test import APIClient

import json


class HealthCheckViewTestCase(TestCase):

    def test_health_check_ok(self):
        """Status route should return OK"""
        client = APIClient()
        path = '/health-check'
        response = client.get(path)
        content = response.json()
        self.assertEqual(content['status'], 'OK')

from application import app
import application.routes
from flask_testing import TestCase
from unittest.mock import patch
from flask import url_for

class TestBase(TestCase):
    def create_app(self):
        return app

class TestView(TestBase):
    @patch('application.routes.choice', return_value='rottweiler')
    def test_get_animal_rottweiler(self, mock_func):
        response = self.client.get(url_for('get_breed'))
        self.assert200(response)
        self.assertIn(b'rottweiler', response.data)
    
    @patch('application.routes.choice', return_value='chihuahua')
    def test_get_animal_chihuahua(self, mock_func):
        response = self.client.get(url_for('get_breed'))
        self.assert200(response)
        self.assertIn(b'chihuahua', response.data)
        
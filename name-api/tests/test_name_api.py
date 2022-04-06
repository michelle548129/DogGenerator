from application import app
from flask_testing import TestCase
from flask import url_for

class TestBase(TestCase):
    def create_app(self):
        return app

class TestView(TestBase):
    def test_get_name_jr(self):
        response = self.client.post(url_for('name'), json={"breed":"chihuahua"})
        self.assert200(response)
        self.assertIn(b'Browny', response.data)
    
    def test_get_name_r(self):
        response = self.client.post(url_for('name'), json={"breed":"rottweiler"})
        self.assert200(response)
        self.assertIn(b'Boston', response.data)
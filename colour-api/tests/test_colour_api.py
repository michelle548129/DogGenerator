from application import app
from flask_testing import TestCase
from flask import url_for

class TestBase(TestCase):
    def create_app(self):
        return app

class TestView(TestBase):
    def test_get_colour_chihuahua(self):
        response = self.client.post(url_for('colour'), json={"breed":"chihuahua"})
        self.assert200(response)
        self.assertIn(b'white', response.data)
    
    def test_get_colour_rottweiler(self):
        response = self.client.post(url_for('colour'), json={"breed":"rottweiler"})
        self.assert200(response)
        self.assertIn(b'black', response.data)
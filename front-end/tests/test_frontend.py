from application import app, db
from application.models import results
from flask import url_for
import requests_mock
from flask_testing import TestCase
import pytest
import application.routes

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',
            DEBUG = True
        )
        return app
        
    def setUp(self):
        sample_result = results(breed='chihuahua', name='Browny')
        db.create_all()
        db.session.add(sample_result)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestView(TestBase):
    def test_get_frontend(self):
        with requests_mock.Mocker() as m:
            m.get('http://breed-api:5000/get-breed', json={"breed":"chihuahua"})
            m.post('http://name-api:5000/noise', json={"name":"Browny"})
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'rottweiler goes Boston', response.data)
            self.assertIn(b'chihuahua goes Browny', response.data)

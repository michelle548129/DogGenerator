from application import app, db
from application.models import results
from flask import render_template
import requests

@app.route('/')
def index():
    breed = requests.get('http://breed-api:5000/breed')
    colour = requests.post('http://colour-api:5000/colour', json=breed.json())
    name = requests.post('http://name-api:5000/name', json=breed.json())
    db.session.add(results(breed=breed.json()["breed"], name=name.json()["name"], colour=colour.json()["colour"]))
    db.session.commit()
    dogs = results.query.all()
    return render_template('index.html', dogs = dogs)
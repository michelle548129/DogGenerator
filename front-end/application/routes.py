from application import app, db
from application.models import results
from flask import render_template
import requests

@app.route('/')
def index():
    breed = requests.get('http://breed-api:5000/breed')
    name = requests.post('http://name-api:5000/name', json=breed.json())
    db.session.add(results(breed=breed.json()["breed"], name=name.json()["name"]))
    db.session.commit()
    dogbreeds = results.query.all()
    dognames = results.query.all()
    return render_template('index.html', dogbreeds = dogbreeds, dognames=dognames)
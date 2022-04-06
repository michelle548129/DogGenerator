from application import app
from flask import jsonify
from random import choice

breeds = ['rottweiler', 'chihuahua', 'chihuahua', 'labrador', 'poodle']

@app.route('/breed', methods=['GET'])
def get_breed():
    breed = choice(breeds)
    return jsonify(breed=breed)
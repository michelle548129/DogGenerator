from application import app
from flask import jsonify
from random import choice

breeds = ['rottweiler', 'dalmatian', 'chihuahua', 'labrador', 'poodle', 'dachshund', 'boxer', 'pug', 'bulldog', 'doberman', 'maltese', 'cockapoo', 'maltipoo']

@app.route('/breed', methods=['GET'])
def get_breed():
    breed = choice(breeds)
    return jsonify(breed=breed)
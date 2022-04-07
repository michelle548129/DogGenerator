from application import app
from flask import request, jsonify

colours = dict(rottweiler='black', dalmatian='spotty', chihuahua='white', labrador='golden', poodle='fluffy')

@app.route('/colour', methods=['POST'])
def colour():
    breed_json = request.get_json()
    breed = breed_json["breed"]
    return jsonify(colour=colours[breed])
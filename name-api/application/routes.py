from application import app
from flask import request, jsonify

names = dict(rottweiler='Boston', dalmatian='Patch', chihuahua='Browny', labrador='Cinnamon', poodle='Spot', dachshund='George', boxer='Henry', pug='Cookie', bulldog='Finn', doberman='Toby', maltese='Bella', cockapoo='Nutmeg', maltipoo='Stella')

@app.route('/name', methods=['POST'])
def name():
    breed_json = request.get_json()
    breed = breed_json["breed"]
    return jsonify(name=names[breed])
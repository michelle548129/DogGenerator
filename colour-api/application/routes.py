from application import app
from flask import request, jsonify

colours = dict(rottweiler='black', dalmatian='spotty', chihuahua='white', labrador='golden', poodle='fluffy', dachshund='sausage-like', boxer='strong', pug='squished-face', bulldog='aggressive', doberman='skinny', maltese='small', cockapoo='brown', maltipoo='curly-haired', bloodhound='rough', chowchow='lazy', hound='grey', collie='multi-colour-eyed', whippet='thin', pomeranian='lion-like', corgi='short', spaniel='loyal', mastiff='big-built', beagle='long-eared', atika='blue-eyed', retriever='friendly', terrier='tiny')

@app.route('/colour', methods=['POST'])
def colour():
    breed_json = request.get_json()
    breed = breed_json["breed"]
    return jsonify(colour=colours[breed])
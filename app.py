from flask import Flask, request
from flask_mongoengine import MongoEngine
from flask import jsonify
import json
import models


app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "projectdb"}

db = MongoEngine(app)


@app.route('/api/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return jsonify(models.User.objects)
    if request.method == 'POST':
        data = request.get_json()

        if models.User.objects(mac_adress=data.get('mac_adress')):
            models.User.objects(mac_adress=data.get('mac_adress')).update(agree=data.get('agree'))
        else:
            models.User.objects.create(**data)
        return app.response_class(status=201)


@app.route('/api/<mac>/', methods=['GET'])
def get_singe(mac):
    if request.method == 'GET':
        try:
            user = models.User.objects(mac_adress=mac)
        except:
            return app.response_class(status=400, response='User not found')

        return jsonify(user)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002)

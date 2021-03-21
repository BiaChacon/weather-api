import json
import requests
import os
from flask import Flask, jsonify, request
from Temperature import Temperature

app = Flask(__name__)

@app.route('/', methods=['GET'])
def check():
    return jsonify("ok")

@app.route('/send', methods=['GET'])
def send_temperature():
    data = Temperature.get_temperature()
    idNode = str(request.query_string).split("=")
    node = idNode[1].replace("'", "")

    obj = {
        "id_node": idNode,
        "sensors": [
            {
                "type": "temperature",
                "value": float(data[0])
            },
            {
                "type": "humidity",
                "value": float(data[1])
            }
        ],
    }

    dado = json.dumps(obj)
    response = requests.post(
        "https://prediction-service-api.herokuapp.com/add", headers={"content-type": "application/json"}, data=dado)

    return jsonify(dado)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

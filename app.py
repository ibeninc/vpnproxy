from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS
from resources.genip import GenerateProxy


app = Flask(__name__)
app.secret_key = "blaaa"
api = Api(app)
CORS(app)

api.add_resource(GenerateProxy, "/getip")


if (
    __name__ == "__main__"
):  # this prevents app from running all its resourses should incase we import app.py in another file
    app.run(port=5000, debug="true")

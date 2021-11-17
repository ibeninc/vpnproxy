from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS
from resources.genip import GenerateProxy


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://rjohzhfo:t8KV22z7hT1rBs-z_a7m_x-zm9B_4ItL@hattie.db.elephantsql.com/rjohzhfo'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['JWT_BLACKLIST_ENABLED'] = True
# app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

app.secret_key = "petral"
api = Api(app)
CORS(app)

api.add_resource(GenerateProxy, "/getip")


if (
    __name__ == "__main__"
):  # this prevents app from running all its resourses should incase we import app.py in another file
    app.run(port=5000, debug="true")

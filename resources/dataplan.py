import os
from flask_restful import Resource
import json
from resources.dataprice import Dataprice

class Dataplan(Resource):

    def get(self, network):
    
        if network == 'mtn':
            return Dataprice.mtn, 200

        elif network == '9mobile':
            return Dataprice.mobile, 200

        elif network == 'airtel':
            return Dataprice.airtel, 200

        elif network == 'glo':
            return Dataprice.glo, 200

        return {"message": "invalid request"}, 500
            
    
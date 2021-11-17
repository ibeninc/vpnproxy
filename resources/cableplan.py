import os
from flask_restful import Resource
import json
from resources.cableprice import Cableprice

class Cableplan(Resource):

    def get(self, provider):
    
        if provider == 'gotv':
            return Cableprice.gotv, 200

        elif provider == 'dstv':
            return Cableprice.dstv, 200

        elif provider == 'startime':
            return Cableprice.startime, 200

        return {"message": "invalid request"}, 500
            
    
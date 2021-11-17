import os
from flask_restful import Resource, reqparse
import requests
import json
import random
import string



class Buydata(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('phone',
    type=str,
    required=True,
    help="phone field cannot be blank."
        )

    parser.add_argument('network',
    type=str,
    required=True,
    help="network field cannot be blank."
        )

    parser.add_argument('code',
    type=str,
    required=True,
    help="datacode field cannot be blank."
        )

    parser.add_argument('amount',
    type=str,
    required=True,
    help="amount field cannot be blank."
        )

    def post(self):
        data = Buydata.parser.parse_args()

        # retrive username from env
        username="petralvtu"

        password="petralvtu@123"

        phone =data['phone']

        network = data['network']

        code = data['code']

        # generate random string for ref
        ref = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
                
        base_url ='https://vtu.ng/wp-json/api/v1/data?username=%s&password=%s&phone=%s&network_id=%s&variation_id=%s' % (username, password, phone, network, code)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        response = requests.get(base_url, headers=headers)
        status= response.status_code
        test=result = response.content
        print(test)
        if status == 200:
            result = response.content
           
            output = json.loads(result)
            print(output)
            return {"message": "success"}, 200
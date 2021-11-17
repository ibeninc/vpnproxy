import os
from flask_restful import Resource, reqparse
import requests
import json
import random
import string



class Buypower(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('phone',
    type=str,
    required=True,
    help="phone field cannot be blank."
        )

    parser.add_argument('meter',
    type=str,
    required=True,
    help="network field cannot be blank."
        )

    parser.add_argument('service',
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
        data = Buypower.parser.parse_args()

        # retrive username from env
        username="petralvtu"

        password="petralvtu@123"

        phone =data['phone']

        meter = data['meter']

        service = data['service']

        amount = data['amount']

        # generate random string for ref
        ref = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
                
        base_url ='https://vtu.ng/wp-json/api/v1/electricity?username=%s&password=%s&phone=%s&meter_number=%s&service_id=%s&variation_id=prepaid&amount=%s' % (username, password, phone, meter, service, amount)
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
import os
from flask_restful import Resource, reqparse
import requests
import json
import random
import string



class Buycable(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('phone',
    type=str,
    required=True,
    help="phone field cannot be blank."
        )

    parser.add_argument('cabletype',
    type=str,
    required=True,
    help="cabletype field cannot be blank."
        )

    parser.add_argument('decorder',
    type=str,
    required=True,
    help="decorder field cannot be blank."
        )

    parser.add_argument('plan',
    type=str,
    required=True,
    help="amount field cannot be blank."
        )

    def post(self):
        data = Buycable.parser.parse_args()

        # retrive username from env
        username="petralvtu"

        password="petralvtu@123"

        phone =data['phone']

        cabletype = data['cabletype']

        decorder = data['decorder']

        plan = data['plan']

        # generate random string for ref
        ref = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
                
        base_url ='https://vtu.ng/wp-json/api/v1/electricity?username=%s&password=%s&phone=%sservice_id=%s&smartcard_number=%s&variation_id=%s' % (username, password, phone, cabletype, decorder, plan)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        response = requests.get(base_url, headers=headers)
        status= response.status_code
        test=result = response.content
        print(response)
        if status == 200:
            result = response.content
           
            # output = json.loads(result)
            # print(output)
            return {"message": "success"}, 200
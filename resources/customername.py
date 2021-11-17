import os
from flask_restful import Resource, reqparse
import requests
import json
import random
import string


class Customer(Resource):
    parser = reqparse.RequestParser()
   
    parser.add_argument('servicetype',
    type=str,
    required=True,
    help="service_type required"
        )
    parser.add_argument('decorder',
    type=int,
    required=True,
    help="amount required"
        )
    

    def post(self):
        incomingdata = Customer.parser.parse_args()


        # generate random string for ref
        ref = ''.join(random.choices(string.ascii_letters + string.digits, k=16))

        
        username="petralvtu"
        password="petralvtu@123"
        decorder = incomingdata['decorder']
        servicetype = incomingdata['servicetype']
        # qdata='https://www.gladtidingsdata.com/api/user/'
        # cablebase = 'https://www.gladtidingsdata.com/api/validateiuc/%s/%s' % (decorder, servicetype)
        # headers = {'Content-type': 'application/json', 'Authorization':"Token  efd2d1a592266f4b0b093c51cc5559977acbe955"}
        
        # # print(cablebase)
        # response = requests.get(qdata, headers)
        # test=result = response
        # print(test)

        cablebase = 'https://vtu.ng/wp-json/api/v1/verify-customer?username=%s&password=%s&customer_id=%s&service_id=%s&variation_id=prepaid' % (username, password, decorder, servicetype)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain',}

        response = requests.get(cablebase, headers)
        status= response.status_code
        test=result = response.content
        
        if status == 200:
            result = response.content
           
            output = json.loads(result)
            final = output['data']
            print(output['data'])
            return {"message": final}, 200
            
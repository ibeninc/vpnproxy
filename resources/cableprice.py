import os
from flask_restful import Resource
import json

class Cableprice(Resource):

    gotv = [
    {
        "code": "gotv-max",
        "amount": 3600,
        "provider": "gotv",
        "descr": "GOtv Max"
        },
    {
        "code": "gotv-jolli",
        "amount": 2460,
        "provider": "gotv",
        "descr": "GOtv Jolli"
    },
    {
        "code": "gotv-jinja",
        "amount": 1640,
        "provider": "gotv",
        "descr": "GOtv Jinja"
    },
    {
        "code": "gotv-smallie",
        "amount": 800,
        "provider": "gotv",
        "descr": "GOtv Smallie"
    }
            ]

    dstv = [
    {
        "code": "dstv-padi",
        "amount": 1850,
        "provider": "dstv",
        "descr": "DStv Padi"
        },
    {
        "code": "dstv-yanga",
        "amount": 2565,
        "provider": "dstv",
        "descr": "DStv Yanga"
    },
    {
        "code": "dstv-confam",
        "amount": 4615,
        "provider": "dstv",
        "descr": "DStv Confam"
    },
    {
        "code": "dstv6",
        "amount": 6200,
        "provider": "dstv",
        "descr": "DStv Asian"
    },
    {
        "code": "dstv79",
        "amount": 7900,
        "provider": "dstv",
        "descr": "DStv Compact"
    },
    {
        "code": "dstv7",
        "amount": 12400,
        "provider": "dstv",
        "descr": "DStv Compact Plus"
    },
     {
        "code": "dstv3",
        "amount": 18400,
        "provider": "dstv",
        "descr": "DStv Premium"
    },
    {
        "code": "dstv10",
        "amount": 20500,
        "provider": "dstv",
        "descr": "DStv Premium Asia"
    }
            ]

    startime = [
    {
        "code": "nova",
        "amount": 900,
        "provider": "startimes",
        "descr": "Startimes Nova"
        },
    {
        "code": "basic",
        "amount": 1700,
        "provider": "startimes",
        "descr": "Startimes Basic"
    },
    {
        "code": "smart",
        "amount": 2200,
        "provider": "startimes",
        "descr": "Startimes Smart"
    },
    {
        "code": "classic",
        "amount": 2500,
        "provider": "startimes",
        "descr": "Startimes Classic"
    },
    {
        "code": "super",
        "amount": 4200,
        "provider": "startimes",
        "descr": "Startimes Super"
    },
   
            ]



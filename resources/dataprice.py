import os
from flask_restful import Resource
import json

class Dataprice(Resource):

    mobile = [
    {
        "code": "9MOB1000",
        "amount": 899,
        "descr": "1.5GB – 30 Days"
        },
    {
        "code": "9MOB2000",
        "amount": 1099,
        "descr": "2GB – 30 Days"
    },
    {
        "code": "9MOB3000",
        "amount": 1349,
        "descr": "3GB – 30 Days"
    },
    {
        "code": "9MOB34500",
        "amount": 1749,
        "descr": "4.5GB – 30 Days"
    },
    {
        "code": "9MOB4000",
        "amount": 3449,
        "descr": "11GB – 30 Days"
    },
    {
        "code": "9MOB5000",
        "amount": 4299,
        "descr": "15GB – 30 Days"
    }
            ]

    airtel = [
    {
        "code": "AIR1000",
        "amount": 939,
        "descr": "1.5GB – 30 Days"
        },
    {
        "code": "Air1200",
        "amount": 1079,
        "descr": "2GB – 30 Days"
    },
    {
        "code": "Air1500",
        "amount": 1429,
        "descr": "3GB – 30 Days"
    },
    {
        "code": "AIR2000",
        "amount": 1889,
        "descr": "4.5GB – 30 Days"
    },
    {
        "code": "AIR2500",
        "amount": 2399,
        "descr": "6GB – 30 Days"
    },
    {
        "code": "Air3000",
        "amount": 2899,
        "descr": "8GB – 30 Days"
    },
     {
        "code": "Air5000",
        "amount": 4699,
        "descr": "15GB – 30 Days"
    },
    {
        "code": "Air100000",
        "amount": 9599,
        "descr": "40GB – 30 Days"
    }
            ]

    glo = [
    {
        "code": "G500",
        "amount": 459,
        "descr": "1GB – 14 Days"
        },
    {
        "code": "G2000",
        "amount": 1799,
        "descr": "5.8GB – 30 Days"
    },
    {
        "code": "G1000",
        "amount": 899,
        "descr": "2GB/2.5GB – 30 Days"
    },
    {
        "code": "G2500",
        "amount": 2199,
        "descr": "7.7GB – 30 Days"
    },
    {
        "code": "G3000",
        "amount": 2699,
        "descr": "10GB – 30 Days"
    },
    {
        "code": "G4000",
        "amount": 3599,
        "descr": "13.25GB – 30 Days"
    },
     {
        "code": "G5000",
        "amount": 4349,
        "descr": "18.25GB – 30 Days"
    },
    {
        "code": "G8000",
        "amount": 6999,
        "descr": "20GB/25GB – 30 Days"
    }
            ]


    mtn = [
    {
        "code": "M1024",
        "amount": 329,
        "descr": "1GB – 30 Days"
        },
    {
        "code": "M2024",
        "amount": 659,
        "descr": "2GB – 30 Days"
    },
    {
        "code": "GIFT500",
        "amount": 449,
        "descr": "2.5GB – 30 Days"
    },
    {
        "code": "5000",
        "amount": 1649,
        "descr": "5GB – 30 Days"
    },
    {
        "code": "GIFT8000",
        "amount": 2599,
        "descr": "8GB – 30 Days"
    },
    {
        "code": "GIFT5000",
        "amount": 4799,
        "descr": "15GB – 30 Days"
    }
            ]

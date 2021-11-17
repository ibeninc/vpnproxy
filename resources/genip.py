import os
from flask_restful import Resource, reqparse
import requests
from bs4 import BeautifulSoup
from random import choice
import json
import time

# pip install requests==2.7.0 to avoid check host name error


class GenerateProxy(Resource):
    def proxy_generator():
        response = requests.get("https://sslproxies.org/")
        soup = BeautifulSoup(response.content, "html5lib")
        proxy = {
            "https": choice(
                list(
                    map(
                        lambda x: x[0] + ":" + x[1],
                        list(
                            zip(
                                map(lambda x: x.text, soup.findAll("td")[::8]),
                                map(lambda x: x.text, soup.findAll("td")[1::8]),
                            )
                        ),
                    )
                )
            )
        }

        return proxy

    def get(self):

        try:
            url = "https://google.com"
            proxy = GenerateProxy.proxy_generator()
            myip = "".join(proxy.values())
            proxies = {
                "https": "https://" + myip,
            }

            print("Proxy currently being used: {}".format(myip))
            response = requests.get("https://google.com", proxies=proxies, timeout=7)
            print(response.status_code)
            print(response)
            return {"ip": myip}
            # return response
            # response = requests.request(get, url, proxies=proxy, timeout=7)
            # if the request is successful, no exception is raised
        except Exception as e:
            print(e)
            time.sleep(10)
            return GenerateProxy.get(self)

        # while True:
        #     try:
        #         url = "https://google.com"
        #         proxy = GenerateProxy.proxy_generator()
        #         myip = "".join(proxy.values())
        #         proxies = {
        #             "https": "https://" + myip,
        #         }
        #         print("Proxy currently being used: {}".format(myip))
        #         response = requests.get(url, proxies=proxies, timeout=7)
        #         print(response)
        #         # response = requests.request(get, url, proxies=proxy, timeout=7)
        #         break
        #         # if the request is successful, no exception is raised
        #     except Exception as e:
        #         print(e)

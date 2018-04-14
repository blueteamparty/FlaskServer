import requests
import json

class Darksky:
    api_key = '1188be2c38f117cbbb215435cf951669'
    forecast_type = ['currently', 'minutely', 'hourly', 'daily']

    @staticmethod
    def forecast(lat, lon, forecast_type = None):
        req_str =  'https://api.darksky.net/forecast/{0}/{1},{2}'.format(Darksky.api_key, str(lat), str(lon))
        print(req_str)
        resp = requests.get(req_str)

        return resp.json()

    @staticmethod
    def time_machine(lat, lon, time):
        req_str =  'https://api.darksky.net/forecast/{0}/{1},{2},{3}'.format(Darksky.api_key, str(lat), str(lon), time)
        print(req_str)
        resp = requests.get(req_str)
        return resp.json()

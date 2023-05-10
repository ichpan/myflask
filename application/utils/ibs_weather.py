#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from fake_useragent import UserAgent

from application.settings import Config


class IbsWeather:

    def __init__(self, city='640121'):
        self.ua = UserAgent()
        self.key = Config.SWEET_KEY
        self.baseurl = 'https://restapi.amap.com/v3/weather/weatherInfo'
        self.headers = {
            'User-Agent': self.ua.random
        }

        self.params = {
            'key': self.key,
            'city': city
        }

    def call_weather_info_api(self):
        resp = requests.get(self.baseurl, params=self.params, headers=self.headers)
        if resp.ok:
            return resp.json()

        return {}

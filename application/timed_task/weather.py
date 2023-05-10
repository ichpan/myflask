#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from fake_useragent import UserAgent

from application.settings import Config
from application.timed_task.celery_app import app


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
            return resp.status_code, resp.json()

        return resp.status_code, {}


@app.task
def get_weather_info():
    """
    从高德地图获取天气信息
    """
    ibs = IbsWeather()
    return ibs.call_weather_info_api()

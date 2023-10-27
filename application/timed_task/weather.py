#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from datetime import datetime as dt

from application.timed_task.celery_app import app
from application.utils.ibs_weather import IbsWeather
from application.utils.mail_server import MailServer


@app.task
def send_weather_info():
    """
    get weather info from ibs.com
    """
    ibs = IbsWeather()
    mail = MailServer()
    weather_info = ibs.call_weather_info_api()

    if weather_info is None:
        logging.error('get weather info error!')
        raise 'get weather info error!'

    live = weather_info['lives'][0]
    date = dt.now().strftime('%Y年%m月%d日')
    greet = f"""
        早上好！王同学,今天是{date},
        中宁县今日☁️天气可能是:{live.get('weather')},
        🌡️温度大概是:{live.get('temperature')}°C左右,
        风向差不多是:{live.get('winddirection')},
        风力估计有:{live.get('windpower')}级,
        那么,早安我的小公主🌹今天也要开心哦🫰🏻
        
        愿你以梦为马，不负韶华！
    """

    mail.send_email(
        to_email='2965345482@qq.com',
        subject='安同学给您请安啦',
        body=greet
    )
    logging.info('邮件发送成功！')

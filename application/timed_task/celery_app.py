#!/usr/bin/env python3
# -*-coding:utf-8 -*-

from datetime import timedelta

from celery import Celery
from celery.schedules import crontab

app = Celery('proj', include=[
    'application.timed_task.tasks',
    'application.timed_task.weather',
])
app.config_from_object('application.settings.celeryconfig')

# 定时任务
app.conf.beat_schedule = {
    "time_teller": {
        "task": "application.timed_task.tasks.time_teller",
        "schedule": crontab(minute="*/1")
    },
    "get_weather": {
        "task": "application.timed_task.weather.get_weather_info",
        "schedule": timedelta(seconds=5)
    }
}

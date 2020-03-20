# -*- coding: utf-8 -*-
# @Time    : 2020-03-20 10:21
# @Author  : Seven
# @File    : test.py
# @Desc    : 定时任务测试

import time

import requests
from django.utils import timezone
from loguru import logger

from etc.celery import app as celery_app


@celery_app.task
def tasks_test():
    logger.info(f"task run {timezone.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


@celery_app.task
def time_consuming_tasks_test():
    logger.info(f"time consuming tasks run {timezone.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    time.sleep(5)
    requests.get("https://www.google.com")

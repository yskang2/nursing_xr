from __future__ import absolute_import, unicode_literals
from time import sleep
from celery import shared_task


"""
배포 전 엔진 정보를 반드시 확인해 주세요.
"""


@shared_task
def priority_task1():
    print("1")
    return "success1"


@shared_task
def priority_task2():
    print("2")
    return "success2"


@shared_task
def priority_task3():
    print("3")
    return "success3"
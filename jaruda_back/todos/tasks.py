from celery import shared_task
import time, random


@shared_task
def beat_test():
    return print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


@shared_task
def print_todo(task):
    time.sleep( random.randint(1,5) )
    return print(f'hello {task}')

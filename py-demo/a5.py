# coding:utf-8
import threading
import time
import random

def worker_func():

    random.seed()
    time.sleep(random.random())


def simple_thread_demo():
    for i in range(10):
        threading.Thread(target=worker_func).start()
    pass

if __name__ == '__main__':

    pass

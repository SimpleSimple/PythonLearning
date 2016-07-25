# coding:utf-8

import time
import random

import queue
import threading

SHARE_Q = queue.Queue()  #构造一个不限制大小的的队列
_WORKER_THREAD_NUM = 3   #设置线程个数s

class MyThread(threading.Thread):
    def __init__(self, func):
        super(MyThread, self).__init__()
        self.func = func

    def run(self):
        self.func()

def worker():
    global SHARE_Q
    while not SHARE_Q.empty():
        item = SHARE_Q.get()
        print("Processing : ", item)
        time.sleep(1)

def main() :
    global SHARE_Q
    threads = []
    for task in range(5) :  #向队列中放入任务
        SHARE_Q.put(task)
    for i in range(_WORKER_THREAD_NUM) :
        thread = MyThread(worker)
        thread.start()
        threads.append(thread)
    for thread in threads :
        thread.join()

if __name__ == '__main__':
    main()

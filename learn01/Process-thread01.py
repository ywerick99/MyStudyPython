#!/usr/bin/env python
# -*- conding:utf-8 -*-

#Process-thread01.py 

import threading
import time

def run(n):
    print("task",n)
    time.sleep(2)

t1=threading.Thread(target=run(1),args=("t1"))
t2=threading.Thread(target=run(2),args=("t2"))
t1.start()
t2.start()



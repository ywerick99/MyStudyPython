#!/usr/bin/env python
# -*- conding:utf-8 -*-

#Process-thread03.py 

import multiprocessing
import time



def run(name):
    time.sleep(1)
    print("hello",name)

if __name__=="__main__":
    for i in range(10):
        # args的参数即使只有一个也要用元祖的形式，参数后面的逗号不能少
        p=multiprocessing.Process(target=run,args=("bob %s" % i,))
        p.start()


#!/usr/bin/env python
# -*- conding:utf-8 -*-
#@File :进度条tqdm-02.py 2018.06.09 0009



from time import sleep
from tqdm import tqdm
# 这里同样的，tqdm就是这个进度条最常用的一个方法
#  里面存一个可迭代对象
for i in tqdm(range(0, 100)):
    # 模拟你的任务
    sleep(0.05)


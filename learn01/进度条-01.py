#!/usr/bin/env python
# -*- conding:utf-8 -*-
#@File :进度条-01.py 2018.06.07 0007


import sys
import time

def progress_bar(total):
    """ 进度条效果 """
    # 获取标准输出
    _output = sys.stdout # 通过参数决定你的进度条总量是多少
    for count in range(0, total + 1):
        # 这里的second只是作为工作量的一种代替
        # 这里应该是有你的主程序,main()
        _second = 0.1
        # 模拟业务的消耗时间
        time.sleep(_second)
        # 输出进度条
        _output.write(f'\rcomplete percent:{count:3.0f}%')
        # 将标准输出一次性刷新

    _output.flush()

progress_bar(100)


#!/usr/bin/env python
# -*- conding: utf-8 -*-

# 文本颜色
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print (bcolors.WARNING + "警告的颜色字体?" + bcolors.ENDC)
print (bcolors.HEADER + "警告的颜色字体?" + bcolors.ENDC)
print (bcolors.OKGREEN + "警告的颜色字体?" + bcolors.ENDC)
print (bcolors.FAIL + "警告的颜色字体?" + bcolors.ENDC)
print (bcolors.BOLD+bcolors.OKBLUE + "警告的颜色字体?" + bcolors.ENDC)

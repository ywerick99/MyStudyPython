#!/usr/bin/env python
# -*- conding:utf-8 -*-

'''题目：输出 9*9 乘法口诀表'''
# 9*9 乘法口诀表
def multiplication():
    for i in range(1,10):
        for j in range(1,i+1):
            print("%d*%d=%d\t" % (j, i, i*j),end="")
        print("")

# 三角
def triangle():
    for i in range(1,11):
        for j in range(1,i+1):
            print("*\t",end="")
        print("")
# 倒三角
def triangle1():
    for i in range(10):
        for j in range(0,i):
            print(" \t",end="")
        for j in range(i,10):
            print("#\t", end="")
        print("")
# 倒三角
def triangle2():
    for i in range(11):
        for j in range(10-i):
            print("\t", end="")
        for j in range(i):
            print("$\t", end="")
        print("")
    print("")

# 倒三角
def triangle3():
    for i in range(1,12):
        print(" \t")
        for j in range(1,12-i):
            print('@\t',end="")
    print("")

triangle()
triangle3()
triangle1()
triangle2()

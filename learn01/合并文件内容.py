#!/usr/bin/env python
# -*- conding:utf-8 -*-

#将两个文件件的内容合并到新的文件
fp = open('test1.txt')
a = fp.read()
fp.close()

fp = open('test2.txt')
b = fp.read()

fp.close()

fp = open('test3.txt', 'w')
fp.write("".join(list(a+ b)))
fp.write("".join(list(a.upper()+ b.upper())))
fp.close()
print("closed")


#!/usr/bin/env python
# -*- conding:utf-8 -*-

#获取路径，文件名，创建目录，创建文件
#读取文件内容，
#复制，修改文件名，移动目录，移动文件
""" os模块的内容
os.open()   //打开文件
os.read()   //读取文件
os.write()  //写入文件
os.close()  //关闭文件
os.mkdir()  //创建文件
os.rmdir()  //删除空目录
os.remove() //删除文件或目录
os.rename() //重命名
os.listdir()    //列出目录下的文件
os.chdir()  //切换目录
os.chmod()  //修改权限
os.chown()  //修改属主
os.getcwd() //获取当前路径
os.path.isfile()    //判断是否为文件
os.path.isdir()     //判断是否为目录
os.path.join()  //合并路径
os.path.split() //分割路径
os.path.abspath()   //获取绝对路径
os.path.basename()  //获取文件名
"""
""" shutil模块的内容
shutil.move()
shutil.copy()
shutil.chown()
"""


import os
import shutil
import time


#创建文件
def make_text_file():
    a=open('test.html',"w")
    a.write("this is how you create a new text file ! ")
    a.close()
#判断文件是否存在
def make_another_file():
    if os.path.isfile("test.html"):
        print("you are trying to create a file that already exists! ")
    else:
        f=open('test.html',"w")
        f.write("this is how you create a new text file ! ")
#文件末尾追加
def add_some_text():
    a=open("test.html","a")
    a.write("here is some additional text! ")
# 追加多行
def even_more_text():
    a=open('test.html',"a")
    a.write("""
    Here is 
    more
    text! 
    """)
#读取文本方式
# a=open("test.html","r")
#print(a.read())
# print(a.readline())
# print(a.readlines())

#获取当前路径
# print(os.path.split(os.getcwd()))
#分割路径
# parent_path,name=os.path.split("C:\Program Files\JetBrains\PyCharm 2018.1.4\lib\src")
#获取父目录
# print(parent_path)
# print(name)
#获取目录下的内容
# print(os.listdir("../"))

#带路径打印目录下的内容
def print_dir(dir_path):
    for name in os.listdir(dir_path):
        print(os.path.join(dir_path,name))

#判断是文件还是目录
# print(os.path.isfile("c:\\windows"))
# print(os.path.isdir("c:\\windows"))

# mod_time=os.path.getatime("D:\\pywork\\python100题\\test.html")
os.path.getatime("test.html")
# print(time.ctime(mod_time))

# 重命名文件
# shutil.move("test.html","test.html.log")
shutil.copy("test.html.log","test.html",)

# 删除文件
# os.remove("test.html.log")
# os.unlink("test.html.log")




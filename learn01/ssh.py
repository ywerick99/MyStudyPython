#!/usr/bin/env python
# -*- conding:utf-8 -*-
#@File :ssh.py 2018.06.09 0009

import paramiko

#创建ssh对象
ssh = paramiko.SSHClient()
#允许连接不在known_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#连接服务器
ssh.connect(hostname="192.168.44.146",port=22,username='root',password="123456")
#执行命令
stdin,stdout,stderr=ssh.exec_command("df -h")

#返回结果
result=stdout.read()
print(result.decode())
#关闭连接
ssh.close()

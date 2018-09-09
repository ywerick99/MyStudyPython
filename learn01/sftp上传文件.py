#!/usr/bin/env python
# -*- conding:utf-8 -*-
#@File :sftp上传文件.py 2018.06.09 0009


import paramiko
transport=paramiko.Transport(("hostname",22))
transport.connect(username='root',password="123456")
sftp=paramiko.SFTPClient.from_transport(transport)
sftp.put('/tmp/location.py',"/tmp/test.py")
sftp.get("remove_path","local_path")
transport.close()

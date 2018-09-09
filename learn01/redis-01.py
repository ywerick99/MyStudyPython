#!/usr/bin/env python
# -*- conding:utf-8 -*-

#redis-01.py
#redis-server /path/to/redis.conf

import redis
r=redis.Redis(host="192.168.44.146",port=6379)
r.set("name","bar")
print(r.get("name"))



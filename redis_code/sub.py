# -*- coding:utf-8 -*-
from xiangmu import RedisBase

obj = RedisBase()
redis_sub = obj.subscribe_msg()
while True:
    msg = redis_sub.parse_response()
    print('msg:%s' % msg)
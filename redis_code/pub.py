# -*- coding:utf-8 -*-

from xiangmu import RedisBase

obj = RedisBase()
msg = 'hello word'
obj.publish_msg(msg)
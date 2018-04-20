# -*- coding:utf-8 -*-

import redis

class RedisBase(object):

    def __init__(self):

        self.__conn = redis.Redis(host='120.77.177.113',port=6379,password=123456)
        self.pub = 'test'
        self.sub = 'test'

    # 发布
    def publish_msg(self,msg):

        self.__conn.publish(self.pub,msg)

    # 订阅
    def subscribe_msg(self):

        pub = self.__conn.pubsub()
        pub.subscribe(self.pub) # 确定订阅通道
        pub.parse_response() # 解析响应
        return pub
# -*- coding: utf-8 -*-

import random,time,Queue
from multiprocessing.manager import BaseManager

def start_Manager(self, url_q, result_q):
    '''
    创建一个分布式管理器
    :param url_q:url队列
    :param result_q:结果队列
    :return:
    '''
    #把创建的两个队列注册在网络上，利用register方法，callbale参数关联了Queue对象，
    #将Queue对象在网络中暴露
    BaseManager.register('get_task_queue', callable=lambda:url_q)
    BaseManager.register('get_result_queue', callable=lambda:result_q)
    #绑定端口8001，设置验证口令"baike"。这个相当于对象的初始化
    manager=BaseManager(address=('',8001),authkey='baike')
    #返回manager对象
    return manager

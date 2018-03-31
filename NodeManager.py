# -*- coding: utf-8 -*-

import time
from multiprocessing.manager import BaseManager
import UrlManager
import DataOutput

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

def url_manager_proc(self, url_q, conn_q, root_url):
    url_manager = UrlManager.UrlManager()
    url_manager.add_new_url(root_url)
    while True:
        while(url_manager.has_new_url()):
            #从URl管理器获取新的URL
            new_url = url_manager.get_new_url()
            #将新的URL发给工作节点
            url_q.put(new_url)
            print('old_url=', url_manager.old_url_size())
            #加一个判断条件，当爬取2000个链接后就关闭，并保存进度
            if(url_manager.old_url_size()>2000):
                #通知爬行节点工作结束
                url_q.put('end')
                print('控制节点发起结束通知！')
                #关闭管理节点，同时存储set状态
                url_manager.save_progress('new_urls.txt', url_manager.new_urls)
                url_manager.save_progress('old_urls.txt', url_manager.old_urls)
                return
        #将从result_solve_proc获取到的URL添加到URL管理器
        try:
            if not conn_q.empty():
                urls = conn_q.get()
                url_manager.add_new_urls(urls)
        except BaseException as e:
            time.sleep(0.1)#延时休息

def result_solve_proc(self, result_q, conn_q, store_q):
    while(True):
        tyr:
            if not result_q.empty():
                content = result_q.get(True)
                if content['new_urls']=='end'
                    #结果分析进程接收通知然后结束！
                    print('结果分析进程接收通知然后结束！')
                    store_q.put('end')
                    return
                conn_q.put(content['new_urls'])#url为set类型
                store_q.put(content['data'])#解析出来的数据为dict类型
            else:
                time.sleep(0.1)#延时休息
        excetp BaseException as e:
            time.sleep(0.1)#延时休息

def store_proc(self, store_q):
    output = DataOutput.DataOutput()
    while True:
        if not store_q.empty():
            data = store_q.get()
            if data=='end':
                print('存储进程接收通知然后结束！')
                output.output_end(output.filepath)
                return
            output.store_data(data)
        else:
            time.sleep(0.1)

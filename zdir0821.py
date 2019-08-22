import argparse
import sys
import os
import requests
import threading
from queue import Queue


#用户输入部分
def userinput():
    """ #argparse模块的作用是用于解析命令行参数，然后创建一个解析对象parser"""
    parser = argparse.ArgumentParser(description="zhaibaba of Zdirscan")             #description 用于展示程序的简要介绍信息，通常包括:这个程序可以做什么、怎么做。
    parser.add_argument("-u","--url",dest="url",help="scan url ex:http://www.baidu.com")
    parser.add_argument("-t","--thread",dest="thread",default=10,type=int,help="The Scan thread  ex:-t 10 ")
    parser.add_argument("-out","--output",action="store_true",help="Save The Result to html")
    args = parser.parse_args()
    return args


#URL部分
def start(url,count=10):


    fdir = open('dir.txt','r',encoding='utf-8')
    result = open('result.txt','w',encoding='utf-8')
    queue = Queue()     #生成一个队列
    print('打开dir.txt')


    #global url_r  # 设置为全局变量

    #URL的处理


     # 对传入的url方便的处理
    if url.endswith("/"):
        url = url.rstrip("/")
    print(url)
    for i in fdir.readlines():
        queue.put(url + i.rstrip('\n'))   #简单拼接



    #线程的部分

    threads = []
    thread_count = count

    for i in range(thread_count):
        threads.append(dirscan(queue))      # 调用多线程Thread继承，创建一个新的class，把线程执行放到这个新的 class里
    for t in threads:
        t.start()                           # 开启多线程
    for t in threads:
        t.join()                            # 等待结束

    # 线程的部分


class dirscan(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while not self.queue.empty():
            url_path = self.queue.get()           # 从队列里获取url

            # 固定的user-agents
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}
            try:
                r = requests.get(url=url_path, headers=headers, timeout=3)
                status_code = r.status_code
                if status_code == 200:
                    print("发现一个",status_code, url_path)
                    if user.report:                          # 看用户传入参数是否需要生成报告，则需要扫描结果输出
                        write_report(url_path)

            except Exception as e:
                print("request有问题")


def write_report(url):
    with open("r1.html", "a") as r:       #a 打开一个文件用于追加。
        r.write('<a href="'+url+'" target="_blank">'+url+'</a><br>')
        r.close()

if __name__ == '__main__':
    user = userinput()
    url = user.url
    thread = user.thread
    if
    start(url,thread)
    print("结束")
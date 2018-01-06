#-*-coding:utf-8-*-
from mongodb_queue import MongoQueue

spider_queue = MongoQueue('baiduSX','json_url02')

for pn in range(1, 1000):
    for cardNum in range(4020, 10000): #4020  重写
        print('pn=' + str(pn) + '---' + str(cardNum))
        url = str(cardNum) + '&iname=&areaName=&pn=' + str( pn * 10)
        spider_queue.push(url)




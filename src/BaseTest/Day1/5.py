#coding:utf-8
'''
Created on 2016年3月20日

@author: yusha
'''
#怎么从集合中查找一个最大或者最小的N个元素
#heapq模块有两个函数：nlargest()，nsmallest()可以完美解决这个问题
import heapq
import random

# nums = [1,8,2,23,7,-4,18,23,42,37,2]
# print(heapq.nlargest(3,nums))
# print(heapq.nsmallest(3,nums))
# 
# #两个函数都能接受一个关键字参数,用于更复杂的数据结构中
# portfolio = [
#     {'name':'IBM','shares':100,'price':91.1},
#     {'name':'AAPL','shares':50,'price':543.22},
#     {'name':'FB','shares':200,'price':21.09},
#     {'name':'HPQ','shares':35,'price':31.75},
#     {'name':'YHOO','shares':45,'price':16.35},
#     {'name':'ACME','shares':75,'price':115.65}
#              ]
# cheap = heapq.nsmallest(2,portfolio,key=lambda s:s['price'])
# expensive = heapq.nlargest(2,portfolio,key=lambda s:s['price'])
# print(cheap)
# print(expensive)

#构建元素个数为 k=5的最小堆代码
heap = []
heapq.heapify(heap)
for i in range(15):
    item = random.randint(10,100)
    print('comeing',item),
    if len(heap)>=5:
        top_item = heap[0]
        if top_item<item:
            top_item = heapq.heappop(heap)
            print('pop',top_item),
            heapq.heappush(heap, item)
            print('push',item),
    else:
        heapq.heappush(heap, item)
        print('push',item),
    pass
    print(heap)
pass
print(heap)

print('sort')
heap.sort()

print(heap)
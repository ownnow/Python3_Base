#coding:utf-8
'''
Created on 2016年3月20日

@author: yusha
'''
from collections import deque

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.append(5)
print(q)

a = deque()
a.append(1)
a.append(2)
a.append(3)
print(a)
a.appendleft(4)
print(a)
a.pop()
print(a)
a.popleft()
print(a)
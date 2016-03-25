#coding:utf-8
'''
Created on 2016年3月20日

@author: yusha
'''
#怎样在两个字典中寻寻找相同点(比如相同的键、相同的值等等)？
a = {
     'x':1,
     'y':2,
     'z':3
     }

b ={
    'w':10,
    'x':11,
    'y':2
    }
#为了寻找两个字典的相同点，可以简单的在两字典的 keys()
# 或者 items() 方法返回结果上执行集合操作
print(a.keys() & b.keys())
print(a.keys() - b.keys())#发现一个键不在字典b中
print(a.items() & b.items())

#以现有字典构造一个排除几个指定键的新字典
c = {key:a[key] for key in a.keys() - {'z','w'}}
print(c)
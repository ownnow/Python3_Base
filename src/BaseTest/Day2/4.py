#coding:utf-8
'''
Created on 2016年3月20日

@author: yusha
'''
#删除序列相同元素并保持顺序
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
a = [1,5,2,1,9,1,5,10]
lists = list(dedupe(a))
print(lists)
print('----'*20)

def dedupe1(items1,key=None):
    seen1 = set()
    for item in items1:
        val = item if key is None else key(item)
        if val not in seen1:
            yield item
            seen1.add(val)
            
b = [
     {'x':1,'y':2},
     {'x':1,'y':3},
     {'x':1,'y':2},
     {'x':2,'y':4}
     ]
ls = list(dedupe1(b, key=lambda d:(d['x'],d['y'])))
print(ls)
print('***'*20)
ls1 = list(dedupe1(b, key=lambda d:d['x']))
print(ls1)
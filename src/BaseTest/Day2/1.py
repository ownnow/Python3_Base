#coding:utf-8
'''
Created on 2016年3月20日

@author: yusha
'''
#一个字典就是一个键对应一个单值的映射。
#如果你想要一个键映射多个值，那么你就需要将这多个值放到另外的容器中，
# 比如列表或者集合里面。比如，你可以像下面这样构造这样的字典
# d = {
#      'a':[1,2,3],
#      'b':[4,5]
#      }
# e = {
#      'a':{1,2,3},
#      'b':{4,5}
#      }
from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(3)
print(d)
print('**'*30)

d1= defaultdict(set)
d1['a'].add(1)
d1['a'].add(2)
d1['b'].add(4)
print(d1)
print('---'*20)

d2 = {}#定义一个空字典
d2.setdefault('a',[]).append(1)
d2.setdefault('a',[]).append(2)
d2.setdefault('b',[]).append(4)
print(d2)
print('$$'*20)
#创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序
#可以使用collections模块中的OrderedDict类
#在迭代操作的时候它会保持元素插入的顺序
from collections import OrderedDict
import json
def ordered_dict():
    d4 = OrderedDict()
    d4['foo']=1
    d4['bar']=2
    d4['spam']=3
    d4['grok']=4
    for key in d4:
        print(key,d4[key])
    jsons1 = json.dumps(d4)
    print(jsons1)
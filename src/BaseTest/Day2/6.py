#coding:utf-8
'''
Created on 2016年3月20日

@author: yusha
'''
#你有一个字典列表，你想根据某个或某几个字典字段来排序这个列表
#通过使用 operator 模块的 itemgetter 函数，可以非常容易的排序这样的数据结构。
#假设你从数据库中检索出来网站会员信息列表，并且以下列的数据结构返回：
rows = [
        {'fname':'Brian','lname':'Jones','uid':1003},
        {'fname':'David','lname':'Beazley','uid':1002},
        {'fname':'John','lname':'Cleese','uid':1001},
        {'fname':'Big','lname':'Jones','uid':1004}
        ]
#根据任意的字典字段来排序输入结果行是很容易实现的，代码示例
from operator import itemgetter
rows_by_fname = sorted(rows,key=itemgetter('fname'))
rows_by_uid = sorted(rows,key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)
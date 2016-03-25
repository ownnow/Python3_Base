#coding:utf-8
'''
Created on 2016年3月20日

@author: yusha
'''
#使用*号来解压字符串，并配合split分割字符
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname,*fields,homedir,sh = line.split(':')
print(uname,homedir,sh)
print(fields)

#解压一些元素然后丢弃它们，你可以使用*—来处理
record = ('ACME',50,123.45,(12,18,2012))
name,*_,(*_,year)=record
print(name)
print(year)

#使用*分割列表，分割成两部分
items = [1,10,7,4,5,9]
head,*tail =items
print(head)
print(tail)

def sum1(items):
    head,*tail = items
    return head + sum(tail) if tail else head
print(sum1(items))
#coding:utf-8
'''
Created on 2016年3月20日

@author: yusha
'''
from collections import deque

def search(lines,pattern,history):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li,previous_lines
        previous_lines.append(li)

if __name__ == '__main__':
    with open('poem.txt') as f:
        for line,prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline,end='')
            print(line,end='')
            print('-'*40)
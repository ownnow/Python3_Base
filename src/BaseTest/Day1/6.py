#coding:utf-8
'''
Created on 2016年3月20日

@author: yusha
'''
import heapq
#如果你想在一个集合中查找最小或最大的N个元素，并且N小于集合元素数量，那么这些函数提供了很好的性能。
# 因为在底层实现里面，首先会先将集合数据进行堆排序后放入一个列表中
nums = [1,8,2,23,7,-4,18,23,42,37,2]
#查找最大的和最小的
mins =min(nums)
maxs =max(nums)
print(mins)
print(maxs)
#前3个最大的和最小的
largest = heapq.nlargest(3, nums)
smallest = heapq.nsmallest(3, nums)
print(largest)
print(smallest)
#对nums进行升序排序
sorts = sorted(nums)
print(sorts)
#如果你想在一个集合中查找最小或最大的N个元素，
#并且N小于集合元素数量，那么这些函数提供了很好的性能。 
#因为在底层实现里面，首先会先将集合数据进行堆排序后放入一个列表中
heapq.heapify(nums)
print(nums)
print('*'*40)
print(sorts)
#sets = sorted(set(nums))
#print(sets)
slices1 = sorted(nums)[:5]
slices2 = sorted(nums)[-3:]
print(slices1)
print(slices2)
#弹出列表中最小的数字，heap[0]永远是最小的元素
#并且剩余的元素可以很容易的通过调用heapq.heappop
#方法得到，该方法会先将第一个元素弹出来，然后用下一个
#最小的元素来取代被弹出元素，比如查找最小的3个元素
heapq.heappush(nums,100)
min1 = heapq.heappop(nums)
min2 = heapq.heappop(nums)
min3 = heapq.heappop(nums)
print(min1)
print(min2)
print(min3)
print('--'*20)
#如果N的大小和集合大小接近的时候，
#通常先排序这个集合然后再使用切片操作会更快点 
print(sorts)
sets = sorted(set(nums))
print(sets)
slices1 = sorted(nums)[:5]
slices2 = sorted(nums)[-3:]
print(slices1)
print(slices2)
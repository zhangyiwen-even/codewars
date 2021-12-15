'''
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements 
with the same value next to each other and preserving the original order of elements.
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
实现函数unique_in_order，该函数以序列作为参数，并返回不包含具有相同值的任何元素的项目列表，这些元素彼此相邻并保留元素的原始顺序。
'''


# 高赞-groupby()函数包含在python的内置模块中，可用其对数据进行分组，通过关键字参数key指定列表元素分组的依据。
# 在python3中，groupby返回一个可迭代的groupby对象，
# 如果将其转换成list，list中每个元素的第二个值也是个可迭代对象。
from itertools import groupby
def unique_in_order(iterable):
    return [key for key,value in groupby(iterable)]
print(unique_in_order('AAAABBBCCDAABBB'))
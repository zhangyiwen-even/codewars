'''
In this kata you have to create all permutations of an input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.
Examples:
permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
在此kata中，您必须创建输入字符串的所有排列并删除重复项（如果存在）。 这意味着，您必须按所有可能的顺序对输入中的所有字母进行混洗。
'''
# 高赞1
# itertools 模块提供的迭代器函数有以下几种类型：
# 无限迭代器：生成一个无限序列，比如自然数序列 1, 2, 3, 4, ...；
# 有限迭代器：接收一个或多个序列（sequence）作为参数，进行组合、分组和过滤等；
# 组合生成器：序列的排列、组合，求序列的笛卡儿积等；

# import itertools
# def permutations(string):
#     return list(''.join(i) for i in set(itertools.permutations(string)))
# print(permutations('aabb'))

# 高赞2 递归思想
# def permutations(string):
#     if len(string) == 1:
#         return list(set(string))
#     first = string[0]
#     rest = permutations(string[1:])
#     result = set()
#     for i in range(0,len(string)):
#         for p in rest:
#             result.add(p[0:i] + first + p[i:])
#     return list(result)
# print(permutations('aabb'))
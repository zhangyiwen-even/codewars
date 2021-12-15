'''
Given two arrays of strings a1 and a2 return a
sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.
#Example 1: a1 = ["arp", "live", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
returns ["arp", "live", "strong"]
#Example 2: a1 = ["tarp", "mice", "bull"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
returns []
Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.
Beware: r must be without duplicates.
Don't mutate the inputs.
给定字符串a1和a2的两个数组，按a1的字符串的字典顺序返回排序的数组r，这些字符串是a2的字符串的子字符串。
'''
# find()方法,索引为-1说明没有查询到
# def in_array(array1, array2):
#     alist = []
#     array1 = set(array1)
#     for i in array1:
#         for j in array2:
#             if j.find(i) != -1:
#                 alist.append(i)
#                 break
#     return sorted(alist)
# print(in_array(["tarp", "mice", "bull"],["lively", "alive", "harp", "sharp", "armstrong"]))

# 高赞
# any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
# 元素除了是 0、空、FALSE 外都算 TRUE。
def in_array(array1, array2):
    return sorted({sub for sub in array1 if any(sub in s for s in array2)})
print(in_array(["tarp", "mice", "bull"],["lively", "alive", "harp", "sharp", "armstrong"]))
print(in_array(["arp", "live", "strong"],["lively", "alive", "harp", "sharp", "armstrong"]))
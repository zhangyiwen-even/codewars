'''
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
It should remove all values from list a, which are present in list b.
array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:
array_diff([1,2,2,2,3],[2]) == [1,3]

您在此kata中的目标是实现一个差异函数，该函数将从另一个列表中减去一个列表并返回结果。
它应该从列表a中删除列表b中存在的所有值。
array_diff（[1,2]，[1]）== [2]
如果b中存在一个值，则必须从另一个中删除所有出现的值：
array_diff（[1,2,2,2,3]，[2]）== [1,3]
'''
#集合 求差集 但有的测试用例过不去
# def array_diff(a, b):
#     aset = set(a)
#     bset = set(b)
#     if len(aset) and len(bset) != 0:
#         return (list(aset - bset))
#     else:
#         if len(aset) != 0:
#             return list(aset)
#         else:
#             return list(bset)
# print(array_diff([1,2,2],[1]))

# def array_diff(a, b):
#     c = []
#     for i in a:
#         if i not in b:
#             c.append(i)
#     return c
# print(array_diff([1,2,2,2,3],[1]))

# 高赞
def array_diff(a, b):
    return [i for i in a if i not in b]
print(array_diff([1,2,2,2,3],[1]))
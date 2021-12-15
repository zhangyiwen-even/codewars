'''
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
顺时针输出二维数组
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:
array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
'''

# 1.先pop第一行[1,2,3]，然后reverse翻转,继续pop掉第一行,然后翻转。
# def snail(snail_map):
#     #pop第一行
#     alist = []
#     while snail_map:
#         alist.append(snail_map.pop(0))
#         if not snail_map or not snail_map[0]:
#             break
#         # return alist
#         turn([[1,2,3],[4,5,6],[7,8,9]])
# def turn(snail_map):
#     row = len(snail_map)
#     column = len(snail_map[0])
#     # return row,column 
#     blist = []
#     for i in range(row):
#         clist = []
#         for j in range(column):
#             clist.append(snail_map[j][i])
#         blist.append(clist)
#     blist.reverse()
#     return blist
# # print(snail([[1,2,3],[4,5,6],[7,8,9]]))
# print(turn([[1,2,3],[4,5,6],[7,8,9]]))


# 剑指offer的解法
# def snail(snail_map):
#     res = []
#     while snail_map:
#         res += snail_map.pop(0)
#         if snail_map and snail_map[0]:
#             for row in snail_map:
#                 res.append(row.pop())
#         if snail_map:
#             res += snail_map.pop()[::-1]
#         if snail_map and snail_map[0]:
#             for row in snail_map[::-1]:
#                 res.append(row.pop(0))
#     return res
# print(snail([[1,2,3],[4,5,6],[7,8,9]]))

# 高赞
# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
# a = [1,2,3]
# b = [4,5,6]
# c = [4,5,6,7,8]
# >>> zipped = zip(a,b)     # 打包为元组的列表
# [(1, 4), (2, 5), (3, 6)]
#>>> zip(a,c)              # 元素个数与最短的列表一致
#[(1, 4), (2, 5), (3, 6)]
#>>> zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
#[(1, 2, 3), (4, 5, 6)]
def snail(snail_map):
    alist = []
    while snail_map:
        alist.extend(list(snail_map.pop(0)))
        snail_map = zip(*snail_map)
        snail_map.reverse()
    return alist
print(snail([[1,2,3],[4,5,6],[7,8,9]]))
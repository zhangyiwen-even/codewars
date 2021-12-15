'''
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
move_zeros([False,1,0,1,2,0,1,3,"a"]) # returns[False,1,1,2,1,3,"a",0,0]
编写一个算法，该算法采用一个数组并将所有零移动到末尾，同时保留其他元素的顺序。
move_zeros（[False，1,0,1,2,0,1,3，“ a”]）＃返回[False，1,1,2,1,3，“ a”，0,0]
'''
# 给定一个整形数组， 将数组中所有的0移动到末尾， 非0项保持不变；
# false为1,0也为1,sorted函数排序有问题
# def move_zeros(array):
#     alist = [i for i in array]
#     # return alist
#     blist = []
#     for x in alist:
#         if x == 0:
#             blist.append(1)
#         else:
#             blist.append(0)
#     return blist
# print(sorted(move_zeros([False,1,0,1,2,0,1,3,"a"])))

# 高赞 
# isinstance()来判断一个对象是否是一个已知的类型，类似 type()。
# isinstance() 与 type() 区别：
# type() 不会认为子类是一种父类类型，不考虑继承关系。
# isinstance() 会认为子类是一种父类类型，考虑继承关系。
# 如果要判断两个类型是否相同推荐使用 isinstance()。
# isinstance(object, classinfo)
# object -- 实例对象。
# classinfo -- 可以是直接或间接类名、基本类型或者由它们组成的元组。

# def move_zeros(array):
#     l = [i for i in array if isinstance(i,bool) or i != 0]
#     return l + [0]*(len(array) - len(l))
# print(move_zeros([False,1,0,1,2,0,1,3,"a"]))

# def move_zeros(array):
#     return sorted(array,key=lambda x: x==0 and type(x) is not bool)
# print(move_zeros([False,1,0,1,2,0,1,3,"a"]))

def move_zeros(array):
    newarr = []
    zeroarr = []
    for i in array:
        if i != 0 or type(i) == bool:
            newarr.append(i)
        else:
            zeroarr.append(i)
    # return newarr + zeroarr
    newarr.extend(zeroarr)
    return newarr
print(move_zeros([False,1,0,1,2,0,1,3,"a"]))
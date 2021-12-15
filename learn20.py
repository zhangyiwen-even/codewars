'''
Hey awesome programmer!
You've got much data to manage and of course you use zero-based and non-negative ID's to make each data item unique!
Therefore you need a method, which returns the smallest unused ID for your next new data item...
Note: The given array of used IDs may be unsorted. For test reasons there may be duplicate IDs, but you don't have to find or remove them!
Go on and code some pure awesomeness!
为下一个新数据项返回最小的未使用ID。
Test.assert_equals(next_id([0,1,2,3,4,5,6,7,8,9,10]), 11)
Test.assert_equals(next_id([5,4,3,2,1]), 0)
Test.assert_equals(next_id([0,1,2,3,5]), 4)
Test.assert_equals(next_id([0,0,0,0,0,0]), 1)
Test.assert_equals(next_id([]), 0)
'''
# #自己
# def next_id(arr):
#     set1 = list(set(arr))
#     # print(set1)
#     for i in range(len(set1)+1):
#         if i not in set1:
#             return(i)
#             break
#     else:
#         return(max(arr)+1)
# print(next_id([5,4,3,2,1]))

#高赞
def next_id(arr):
    t = 0
    while t in arr:
        t += 1
    return t 
print(next_id([5,4,3,2,1]))
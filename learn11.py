'''
You are given an array (which will have a length of at least 3, but could be very large) containing integers. 
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. 
Write a method that takes the array as an argument and returns this "outlier" N.
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)
[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
您将获得一个包含整数的数组（长度至少为3，但可能会非常大）。
除了单个整数N之外，该数组要么完全由奇数整数组成，要么完全由偶数整数组成。
编写一个将数组作为参数并返回此“异常值” N的方法。
[2，4，0，100，4，11，2602，36]
应该返回：11（唯一的奇数）
[160，3，1719，19，11，13，-21]
应该返回：160（唯一的偶数）
'''

# def find_outlier(integers):
#     jishu = oushu = []
#     for i in range(len(integers)):
#         if integers[i] % 2 == 0:
#             oushu.append(integers[i])
#         else:
#             jishu.append(integers[i])
#     if len(jishu) == 1:
#         print(''.join(jishu))
#     else:
#         print(''.join(oushu))
# find_outlier('[160，3，1719，19，11，13，-21]')

def find_outlier(integers):
    # jishu = oushu = []
    oushu = [i for i in integers if i % 2 == 0]
    # print(oushu)
    jishu = [i for i in integers if i % 2 == 1]
    # print(jishu)
    if len(oushu) == 1:
        print(oushu[0])
    else:
        print(jishu[0])
find_outlier([2,4,0,100,4,11,2602,36])

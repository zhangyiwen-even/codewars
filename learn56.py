'''
Define a function that takes an integer argument and returns logical value true or false depending on if the integer is a prime.
Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.
Requirements
You can assume you will be given an integer input.
You can not assume that the integer will be only positive. You may be given negative numbers as well (or 0).
NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out. Numbers go up to 2^31 (or similar, depends on language version). 
Looping all the way up to n, or n/2, will be too slow.
'''
# 定义列表 判断列表元素个数是否为空 超时
# def is_prime(num):
#     alist = [int(i) for i in range(2,num) if num % i == 0]
#     if alist:
#         return False
#     elif num <= 1:
#         return False
#     else:
#         return True
# print(is_prime(13))

# 直接判断 超时
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2,num):
#         if num % i == 0:
#             return False
#     else:
#         return True
# print(is_prime(0))

# 3.逻辑有误
# def is_prime(num):
#     for i in range(2,num):
#         if num % 2 == 0:
#             return False
#         break
#     if num < 2:
#         return False
#     else:
#         return True
# print(is_prime(75))

# 4.gmpy2.is_prime(num) 用于素性检测
# import gmpy2
# def is_prime(num):
#     return gmpy2.is_prime(num) if num > 0 else False
# print(is_prime(75))

# 5.math.floor表示返回小于或等于指定数字的最大整数的数字。
# Math.floor( 45.95); 
# // 45 
# Math.floor( 45.05); 
# // 45 
# import math
# def is_prime(num):
#     if num < 2:return False
#     if (num in [2,3]):return True
#     if (num % 6 not in [1,5]):return False
#     for i in range(3,int(math.floor(math.sqrt(num)))+1):
#         if num % i == 0:
#             return False
#     return True
# print(is_prime(11))

# 6.
from math import sqrt
def is_prime(num):
    if num <= 1:
        return False
    i = 2
    while i <= sqrt(num):
        if num % i == 0:
            return False
        i += 1
    return True
print(is_prime(-1))

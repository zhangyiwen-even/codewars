'''
创建一个名为divisors / Divisors的函数，该函数采用整数n> 1并返回一个数组，
该数组具有从最小到最大的所有整数除数（除了1和数字本身）。 如果数字为质数，则返回字符串'（integer）为质数'（在C＃中为null）
（在Haskell中使用String a，在Rust中使用Result <Vec <u32>，String>）。

例：
除数（12）; ＃应返回[2,3,4,6]
除数（25）; ＃应返回[5]
除数（13）; ＃应返回“ 13是素数”
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's 
divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the 
string '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

Example:
divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"
'''
#可以判断是否为质数，但输出列表有问题，只能输出第一个。
# def divisors(integer):
#     alist = []
#     for i in range(2,integer):
#         if (integer % i) == 0:
#             alist.append(i)
#             print(alist)
#         else:
#             print(integer,'is prime')
# divisors(26) 


# def divisors(integer): 
#     for i in range(2,integer):
#         if (integer % i) != 0:
#             print(integer,'is prime')
#         break
#     # list1 = [i for i in range(2,integer) if (integer % i) == 0]
#     # print(list1)
#     print([i for i in range(2,integer) if (integer % i) == 0])
#divisors(13) 

def divisors(integer):
    alist = [int(i) for i in range(2,integer) if integer % i == 0]
    if alist:
        print(alist)
    else:
        print(integer,'is not prime')
divisors(13)
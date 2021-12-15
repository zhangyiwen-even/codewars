'''
For this Kata you will have to forget how to add two numbers together.
The best explanation on what to do for this kata is this meme:
In simple terms, our method does not like the principle of 
carrying over numbers and just writes down every number it calculates :-)
You may assume both integers are positive integers
对于此卡塔，您将不得不忘记如何将两个数字相加。
这个模因最好的解释是做这个模因：
简而言之，我们的方法不喜欢结转数字的原理，只是写下它计算出的每个数字:-)
您可以假设两个整数都是正整数
'''
# python中divmod函数
# Python divmod() 函数接收两个数字类型（非复数）参数，返回一个包含商和余数的元组(a // b, a % b)。
# 在 python 3.x 版本该函数不支持复数。
# 函数语法
# divmod(a, b)
# 参数说明：
# a: 数字，非复数。
# b: 数字，非复数。
# 如果参数 a 与 参数 b 都是整数，函数返回的结果相当于 (a // b, a % b)。
# 如果其中一个参数为浮点数时，函数返回的结果相当于 (q, a % b)，q 通常是 math.floor(a / b)，但也有可能是 1 ，比小，不过 q * b + a % b 的值会非常接近 a。
# 如果 a % b 的求余结果不为 0 ，则余数的正负符号跟参数 b 是一样的，若 b 是正数，余数为正数，若 b 为负数，余数也为负数，并且 0 <= abs(a % b) < abs(b)。

# 16+18 = 214
# def add(a,b):
#     s = ""
#     while a+b:
#         a,p = divmod(a,10)
#         b,q = divmod(b,10)
#         s = str(p+q) + s
#     return int(s or '0')
# print(add(16,18))

# zfill() 返回指定长度的字符串，原字符串右对齐，前面填充0。
# def add(a,b):
#     if a > b:
#         b = str(b).zfill(len(str(a)))
#         a = str(a)
#     else:
#         a = str(a).zfill(len(str(b)))
#         b = str(b)
#     return int(''.join([str(int(a[i]) + int(b[j])) for i in range(len(a)) for j in range(len(b)) if i == j]))
# print(add(116,19))

# def add(a,b):
#     result = ""
#     while a or b:
#         result = f"{a % 10 + b % 10}{result}"
#         a , b = a // 10 , b // 10
#     return int(result or 0)
# print(add(14,19))
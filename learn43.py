'''
The prime numbers are not regularly spaced. For example from 2 to 3 the gap is 1. From 3 to 5 the gap is 2. From 7 to 11 it is 4. Between 2 and 50 we have the following pairs of 2-gaps primes: 3-5, 5-7, 11-13, 17-19, 29-31, 41-43
A prime gap of length n is a run of n-1 consecutive composite numbers between two successive primes (see: http://mathworld.wolfram.com/PrimeGaps.html).
We will write a function gap with parameters:
g (integer >= 2) which indicates the gap we are looking for
m (integer > 2) which gives the start of the search (m inclusive)
n (integer >= m) which gives the end of the search (n inclusive)
In the example above gap(2, 3, 50) will return [3, 5] or (3, 5) or {3, 5} which is the first pair between 3 and 50 with a 2-gap.
So this function should return the first pair of two prime numbers spaced with a gap of g between the limits m, n if these numbers exist otherwise nil or null or None or Nothing (depending on the language).
In C++ return in such a case {0, 0}. In F# return [||]. In Kotlin return []
#Examples: gap(2, 5, 7) --> [5, 7] or (5, 7) or {5, 7}
gap(2, 5, 5) --> nil. In C++ {0, 0}. In F# [||]. In Kotlin return[]`
gap(4, 130, 200) --> [163, 167] or (163, 167) or {163, 167}
([193, 197] is also such a 4-gap primes between 130 and 200 but it's not the first pair)
gap(6,100,110) --> nil or {0, 0} : between 100 and 110 we have 101, 103, 107, 109 but 101-107is not a 6-gap because there is 103in between and 103-109is not a 6-gap because there is 107in between.
Note for Go
For Go: nil slice is expected when there are no gap between m and n. Example: gap(11,30000,100000) --> nil
质数没有规则的间隔。例如，从2到3的间隙为1。从3到5的间隙为2。从7到11的间隙为4。在2到50之间，我们有以下两对2间隙素数：3-5、5-7 ，11-13、17-19、29-31、41-43
长度为n的素数间隔是两个连续素数之间n-1个连续复合数的行程
我们将编写一个带有参数的函数间隙：
g（整数> = 2）表示我们正在寻找的缺口
m（整数> 2）给出搜索的开始（包括m）
n（整数> = m），表示搜索结束（包括n）
Test.describe("Gap")
Test.it("Basic tests")
Test.assert_equals(gap(2,100,110), [101, 103])
Test.assert_equals(gap(4,100,110), [103, 107])
Test.assert_equals(gap(6,100,110), None)
Test.assert_equals(gap(8,300,400), [359, 367])
Test.assert_equals(gap(10,300,400), [337, 347])
'''

# def gap(g,m,n):
#     result1 = []
#     result2 = []
#     # 判断两数之间所有的素数
#     for i in range(m,n):
#         t_or_f =False
#         for j in range(2,int(i/2)):
#             if i%j==0:
#                 t_or_f = True
#                 break
#         if t_or_f ==False:
#             result1.append(i)
#     return result1
#     #判断满足条件的素数
#     # result1 = [101, 103, 107, 109]
#     for x in range(len(result1)+1):
#         if result1[x] - result1[x-1] == g:
#             result2.append(result1[x])
#     return result2
# print(gap(2,100,110))

# 高赞
# def gap(g, m, n):
#     previous_prime = n
#     for i in range(m, n + 1):
#         if is_prime(i):
#             if i - previous_prime == g: 
#                 return [previous_prime, i]
#             previous_prime = i
#     return None
            
# def is_prime(n):
#     for i in range(2, int(n**.5 + 1)):
#         if n % i == 0:
#             return False
#     return True
# print(gap(6,100,110))

# 高赞
# （&，|）和（and，or）是两组比较相似的运算符，用在“与”/ “或”上，在用法上有些许区别。
# （&，|）和（and，or）是用来比较两组变量的，格式基本上是：
# a & b
# a | b
# a and b
# a or b
# 如果a，b是数值变量， 则&， |表示位运算， and，or则依据是否非0来决定输出
# def gap(g,m,n):
#     prev = 2
#     for x in range(m|1,n+1,2):
#         if all(x%d for d in range(3,int(x**.5) + 1,2)):
#             if x - prev ==g:
#                 return [prev,x]
#             prev = x
# print(gap(6,100,110))


def gap(g,m,n):
    primary_prime = n
    for i in range(m,n+1):
        if isprime(i):
            if i - primary_prime == g:
                return [primary_prime,i]
            primary_prime = i
    return None

def isprime(n):
    for i in range(2,int(n**.5 + 1)):
        if n % i == 0:
            return False
    return True
print(gap(2,100,110))
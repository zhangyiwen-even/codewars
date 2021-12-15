'''
Your task is to create functionisDivideBy (or is_divide_by) to check if an integer number is divisible by each out of two arguments.
A few cases:
(-12, 2, -6)  ->  true
(-12, 2, -5)  ->  false

(45, 1, 6)    ->  false
(45, 5, 15)   ->  true

(4, 1, 4)     ->  true
(15, -5, 3)   ->  true
'''
# def is_divide_by(number, a, b):
#     if number % a == 0 and number % b == 0:
#         return True
#     else:
#         return False
# print(is_divide_by(-12, 2, -5))

# def is_divide_by(number,a,b):
#     return number % a == 0 and number % b == 0
# print(is_divide_by(-12, 2, -5))

'''
This kata is from check py.checkio.org
You are given an array with positive numbers and a number N. You should find the N-th power of the element in the array with the index N. If N is outside of the array, then return -1. Don't forget that the first element has the index 0.
Let's look at a few examples:

array = [1, 2, 3, 4] and N = 2, then the result is 3^2 == 9;
array = [1, 2, 3] and N = 3, but N is outside of the array, so the result is -1.
这个kata来自check py.checkio.org
您将获得一个带有正数和N的数组。您应该在索引为N的数组中找到元素的N次方。如果N在数组之外，则返回-1。 不要忘记第一个元素的索引为0。
让我们看几个例子：
数组= [1、2、3、4]且N = 2，则结果为3 ^ 2 == 9;
array = [1,2,3]且N = 3，但是N在数组之外，因此结果为-1。
'''
# def index(array, n):
#     len1 = len(array)
#     if n+1 > len1:
#         return -1
#     else:
#         return (array[n]) ** n
# print(index([1,2,3,4],2))
# print(index([1, 3, 10, 100],3))

# def index(array,n):
#     try:
#         return array[n] ** n
#     except:
#         return -1
# print(index([1, 3, 10, 100],3))

'''
Born a misinterpretation of this kata, your task here is pretty simple: 
given an array of values and an amount of beggars, you are supposed to return an array with the sum of what each beggar brings home, 
assuming they all take regular turns, from the first to the last.
For example: [1,2,3,4,5] for 2 beggars will return a result of [9,6], 
as the first one takes [1,3,5], the second collects [2,4].
The same array with 3 beggars would have in turn have produced a better out come for the second beggar: [5,7,3],
as they will respectively take [1,4], [2,5] and [3].
Also note that not all beggars have to take the same amount of "offers", meaning that the length of the array is not necessarily a multiple of n; 
length can be even shorter, in which case the last beggars will of course take nothing (0).
Note: in case you don't get why this kata is about English beggars, then you are not familiar on how religiously queues are taken in the kingdom ;)

由于对这个kata有误解，因此您的任务非常简单：给定一个值数组和多个乞g，假设每个乞g定期轮换，假设您将返回一个包含每个乞brings带回家的总和的数组。 从头到尾。
例如：2个乞[的[1,2,3,4,5]将返回结果[9,6]，因为第一个乞takes取[1,3,5]，第二个乞[取[2,4]。
具有3个乞g的相同数组反过来又会为第二个乞produced产生更好的结果：[5,7,3]，因为它们分别取[1,4]，[2,5]和[3]。
另请注意，并非所有乞g都必须采取相同数量的“优惠”，这意味着数组的长度不一定是n的倍数； 长度甚至可以更短，在这种情况下，最后的乞g当然不会采取任何行动（0）。
注意：如果您不知道为什么这个kata是关于英语乞g的，那么您不熟悉在王国中如何虔诚地排队；）
Test.describe("Basic tests")
Test.assert_equals(beggars([1,2,3,4,5],1),[15])
# [1+2+3+4+5]
Test.assert_equals(beggars([1,2,3,4,5],2),[9,6])
# [1+3+5,2+4]
Test.assert_equals(beggars([1,2,3,4,5],3),[5,7,3])
# [1+4,2+7,3]
Test.assert_equals(beggars([1,2,3,4,5],6),[1,2,3,4,5,0])
# [1,2,3,4,5,0]
Test.assert_equals(beggars([1,2,3,4,5],0),[])
'''
# def beggars(values, n):
#     if n == 0:
#         return []
#     elif n > len(values):
#         return values + [0]
#     else:
        
# print(beggars([1,2,3,4,5],6))

# def beggar(values,n):
#     return [sum(values[i::n]) for i in range(n)]
# print(beggar([1,2,3,4,5],10))

# def beggars(values,n):
#     if n == 0:
#         return []
#     i = 0 
#     take = []
#     for x in range(n):
#         take.append(0)
#     for val in values:
#         take[i%n] = take[i%n] + val
#         i = i + 1
#     return take
# print(beggars([1,2,3,4,5],6))

# def beggars(values:list,n:int):
#     if n < 1:
#         return []
#     beggars = [0] * n:
#     for i,v in enumerate(values):
#         beggars[i%n] += v
#     return beggars

# 匿名函数
beggars = lambda values,n:[sum(values[i::n]) for i in range(n)]
print(beggars([1,2,3,4,5],2))
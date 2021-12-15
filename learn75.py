'''
Bob is bored during his physics lessons so he's built himself a toy box to help pass the time. 
The box is special because it has the ability to change gravity.
There are some columns of toy cubes in the box arranged in a line. The i-th column contains a_i cubes. 
At first, the gravity in the box is pulling the cubes downwards. When Bob switches the gravity,
it begins to pull all the cubes to a certain side of the box, d, 
which can be either 'L' or 'R' (left or right). 
Below is an example of what a box of cubes might look like before and after switching gravity.
'''

# def flip(d, a):
#     if d == 'R':
#         a.sort()
#         return a
#     elif d == 'L':
#         a.sort(reverse=True)
#         return a
# print(flip('L', [1, 4, 5, 3, 5]))

# def double_integer(i):
#     return 2 * i
# print(double_integer(3))

# def areYouPlayingBanjo(name):
#     if name[0] == 'R' or name[0] == 'r':
#         return name + " plays banjo"
#     else:
#         return name + " does not play banjo"
# print(areYouPlayingBanjo("Rrmartin"))

# def invert(lst):
#     if len(lst) == 0:
#         return []
#     else:
#         return [-i for i in lst]
# print(invert([-1,2,-3,4,-5]))

# def summation(num):
#     sum = 0
#     for i in range(1,num+1):
#         sum += i
#     return sum
# print(summation(100))

# def greet(name):
#     # return 'hello, ' + name + ' how are you doing today?'
#     return "Hello, {} how are you doing today?".format(name)
# print(greet('Ryan'))

# def arr(n=0):
#     if n == 0 or n == None:
#         return [] 
#     else:
#         return [i for i in range(0,n)]
# print(arr(6))

# def sakura_fall(v):
#     if v > 0:
#         return int(400/v)
#     else:
#         return 0
# print(sakura_fall(10))

# def solution(a, b):
#     if len(a) > len(b):
#         return b + a + b
#     else:
#         return a + b + a
# print(solution("45","1"))

'''
Write function parse_float which 
takes a string/list and returns a number or 'none' 
if conversion is not possible.
'''
# def parse_float(string):
#     if string.isalpha():
#         return None
#     else:
#         return float(string)
# print(parse_float("234.054"))

# def parse_float(string):
#     try:
#         return float(string)
#     except:
#         return None
# print(parse_float('a'))

# def parse_float(string):
#     try:
#         return float(string)
#     except(ValueError,TabError):
#         return None
# print(parse_float('a'))

# def disemvowel(string):
#     vowel = ['a','e','i','o','u','A','E','I','O','U']
#     alist = []
#     for i in string:
#         for j in i:
#             if j not in vowel:
#                 alist.append(j)
#     return ''.join(alist)
# print(disemvowel("This website is for losers LOL!"))

# def disemvowel(string):
#     for i in "aeiouAEIOU":
#         string = string.replace(i,'')
#     return string
# print(disemvowel("This website is for losers LOL!"))

# import re
# def disemvowel(string):
#     return re.sub(r"[aeiouAEIOU]","",string)
# print(disemvowel("This website is for losers LOL!"))

'''
In this Kata, you will be given an array of numbers in which two numbers occur once and the rest occur only twice. 
Your task will be to return the sum of the numbers that occur only once.
For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, and their sum is 15.
More examples in the test cases.
Good luck!
If you like this Kata, please try:
'''

# def repeats(arr):
#     alist = []
#     for i in arr:
#         if arr.count(i) == 1:
#             alist.append(i)
#     return sum(alist)
# print(repeats([5, 10, 19, 13, 10, 13]))

# def repeats(arr):
#     return sum([i for i in arr if arr.count(i) == 1])
# print(repeats([5, 10, 19, 13, 10, 13]))


# int("001001", 2)可以把二进制转换为十进制。
# 001001是二进制，记得要加上双引号。
# 数字2表示"001001"为二进制。
# 如果输入的不是二进制数字就会报错。

# def binary_array_to_number(arr):
#     return int("".join(map(str,arr)),2)
# print(binary_array_to_number([1,0,0,1]))

# def binary_array_to_number(arr):
#     s = 0
#     for digit in arr:
#         s = s * 2 + digit
#     return s
# print(binary_array_to_number([1,0,0,1]))

# def is_even(n): 
#     if n % 2 == 0:
#         return True
#     else:
#         return False
# print(is_even(22222222))

# def is_even(n): 
#     return n % 2 == 0
# print(is_even(0))


# def array_plus_array(arr1,arr2):
#     # return sum(arr1)+sum(arr2)
#     # return sum(arr1+arr2)
# print(array_plus_array([1, 2, 3], [4, 5, 6]))

# def high_and_low(numbers):
#     alist = numbers.split()
#     blist = []
#     for i in alist:
#         blist.append(int(i))
#     # return blist
#     maxnum = max(blist)
#     minnum = min(blist)
#     str1 = str(maxnum) + ' ' + str(minnum) 
#     return str1
# print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))

# def high_and_low(numbers):
#     nn = [int(s) for s in numbers.split(" ")]
#     return "%i %i" % (max(nn),min(nn))
# print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")) 

# def two_oldest_ages(ages):
#     max1 = max(ages)
#     ages.remove(max1)
#     max2 = max(ages)
#     return [max2,max1]
# print(two_oldest_ages([1, 5, 87, 45, 8, 8]))

# def two_oldest_ages(ages):
#     return sorted(ages)[-2:]
# print(two_oldest_ages([1, 5, 87, 45, 8, 8]))

# def solve(s):
#     return max(map(len,''.join(c if c in 'aeiou' else ' ' for c in s).split()))
# print(solve('aeiowooo'))

# from re import findall
# def solve(s):
#     return max(map(len,findall("[aeiou]+",s)))
# print(solve('aeiowooo'))

# def find_longest(string):
#     spl = string.split(" ")
#     longest = 0
#     i=0
#     while (i > len(spl)):
#         if (len(spl) > longest): 
#             longest = len(string)
#     return longest
# print(find_longest('Sausage chops'))

# Python swapcase() 方法用于对字符串的大小写字母进行转换。
# def to_alternating_case(string):
#     return string.swapcase()
# print(to_alternating_case('hello World'))

# def to_alternating_case(string):
#     astr = ""
#     for i in string:
#         if i.isupper():
#             astr += i.lower()
#         else:
#             astr += i.upper()
#     return astr
# print(to_alternating_case('zhang EvEn'))

# def get_real_floor(n):
#     if n <= 0:
#         return n
#     # elif n == 1:
#     #     return 0
#     # elif n > 1 and n <= 13:
#     #     return n - 1
#     elif n < 13:
#         return n - 1
#     else:
#         return n - 2
# print(get_real_floor(1))

# def digitize(n):
#     alist = [int(i) for i in str(n)]
#     return alist[::-1]
# print(digitize(1234))

# def sum_mix(arr):
#     alist = [int(i) for i in arr]
#     return sum(alist)
# print(sum_mix([9, 3, '7', '3']))

# def sum_mix(arr):
#     return sum(map(int,arr))
# print(sum_mix([9, 3, '7', '3']))

# def square_sum(numbers):
#     alist= [int(i) ** 2 for i in numbers]
#     return sum(alist)
# print(square_sum([1,2]))


# def remove_char(s):
#     if len(s) <= 2:
#         return ""
#     else:
#         return s[1:-1]
# print(remove_char('pl'))


# def mirror(data):
#     data1 = sorted(data)
#     # return data
#     data2 = data1[::-1]
#     data3 = data2[1::]
#     return data1 + data3
# print(mirror([-3, 15, 8, -1, 7, -1]))

# def descending_order(num):
#     alist = [i for i in str(num)]
#     blist = sorted(alist,reverse=True)
#     return int(''.join(blist))
# print(descending_order(42145))


# def sort_array(source_array):
#     alist = []
#     for i in source_array:
#         if i % 2 != 0:
#             return alist.append(sorted(i))
#         else:
#             return alist.append(i)
# print(sort_array([5, 3, 2, 8, 1, 4]))



# def reverse_seq(n):
#     alist = []
#     for i in range(1,n+1):
#         alist.append(i)
#     return alist[::-1]
# print(reverse_seq(5))

# def quarter_of(month):
#     if month in [1,2,3]:
#         return 1
#     elif month in [4,5,6]:
#         return 2
#     elif month in [7,8,9]:
#         return 3
#     else:
#         return 4
# print(quarter_of(11))

# def quarter_of(month):
#     if month in range(1,4):
#         return 1
#     elif  month in range(4,7):
#         return 2
#     elif month in range(7,10):
#         return 3
#     elif month in range(10,13):
#         return 4
# print(quarter_of(10))

# def check(a, x): 
#     if x in a:
#         return True
#     else:
#         return False
# print(check([66, 101], 66))

# def super_size(n):
#     alist = []
#     for i in str(n):
#         alist.append(i)
#         alist.sort(reverse=True)
#     return int(''.join(alist))
# print(super_size(1234567))

# def check_for_factor(base, factor):
#     if base % factor == 0:
#         return True
#     else:
#         return False
# print(check_for_factor(9, 2))

# def mouth_size(animal): 
#     if len(animal.lower()) % 2 == 0:
#         return "wide"
#     else:
#         return "small"
# print(mouth_size("toucan"))

# def mouth_size(animal):
#     if animal.lower() == 'alligator':
#         return 'small'
#     else:
#         return 'wide'
# print(mouth_size("alligatr"))

# def even_or_odd(s):
#     alist = []
#     for i in s:
#         alist.append(i)
#     # return alist
#     jisum = ousum = 0
#     for j in alist:
#         if int(j) % 2 == 0:
#             ousum += int(j)
#         else:
#             jisum += int(j)
#     if ousum < jisum:
#         return 'Odd is greater than Even'
#     elif jisum < ousum:
#         return 'Even is greater than Odd'
#     else:
#         return 'Even and Odd are the same'
# print(even_or_odd('1112'))


# def even_or_odd(s):
#     diff = 0
#     for char in s:
#         num = int(char)
#         diff += (-1) ** (num % 2) * num
#     return 'Even and Odd are the same' if diff == 0 else 'Even is greater than Odd' if diff > 0 else 'Odd is greater than Even'
# print(even_or_odd('223'))

# def divisible_by(numbers, divisor):
#     alist = []
#     for i in numbers:
#         if i % divisor == 0:
#             alist.append(i)
#     return alist
# print(divisible_by([0],4))

# def set_alarm(employed, vacation):
#     if employed:
#         if vacation:
#             return False
#         return True
#     return False
# print(set_alarm(True, True))   

# def set_alarm(employed, vacation):
#     return employed == True and vacation == False
# print(set_alarm(True,True))

# def hoop_count(n):
#     if n < 10:
#         return 'Keep at it until you get it'
#     else:
#         return 'Great, now move on to tricks'

# def unusual_five():
#     return len("five!")
# print(unusual_five())


# ord函数

# def square(x):
#     return x * 2

# def maps(a):
#     return list(map(square,a))

# print(maps([1,2,3,4,5]))

# def maps(a):
#     return list(map(lambda x: x*2,a))
# print(maps([1,2,3,4,5]))

# def remove_url_anchor(url):
#     url1 = url.split('#',1)
#     return url1[0]
# print(remove_url_anchor("www.codewars.com/katas/?page=1#about"))

# def nth_smallest(arr, pos):
#     alist = sorted(arr,reverse=False)
#     return alist[pos-1]
# print(nth_smallest([15,20,7,10,4,3],3))

# def evens_and_odds(n):
#     if n % 2 == 0:
#         bin1 = bin(n)
#         return bin1.split('b')[1]
#     else:
#         hex1 = hex(n)
#         return hex1.split('x')[1]
# print(evens_and_odds(4))

# def tidyNumber(n):
#     alist = [int(i) for i in str(n)]
#     blist = sorted(alist,reverse=False)
#     if alist == blist:
#         return True
#     else:
#         return False
# print(tidyNumber(9672))

# def row_weights(array):
#     if len(array) == 2:
#         return tuple(array)
#     elif len(array) == 1:
#         return array[0],1
#     elif len(array) == 0:
#         return (0,0)
#     elif len(array) > 2:
#         alist = jishu = oushu = []
#         jishu = array[::2]
#         ouhsu = array[1::2]
#         sum1 = sum(jishu)
#         sum2 = sum(ouhsu)
#         alist.append(sum1)
#         alist.append(sum2)
#         return tuple(alist)
# print(row_weights([70]))

# def row_weights(array):
#     return sum(array[::2]),sum(array[1::2])
# print(row_weights([29,83,67,53,19,28,96]))


# def min_value(digits):
#     aset = sorted(list(set(digits)))
#     alist = [str(x) for x in aset]
#     return int(''.join(alist))
# print(min_value([4, 8, 1, 4]))

# def max_gap(numbers):
#     alist = sorted(numbers)
#     # return alist
#     return max(b-a for a,b in zip(alist,alist[1:]))
# print(max_gap([13,10,2,9,5]))

# import numpy
# def max_gap(numbers):
#     return max(numpy.diff(sorted(numbers)))

# def minimum_steps(numbers, value):
#     sum1 = sum(numbers)
#     for i in numbers:
#         if i > value:
#             return 0
#         elif sum1 > value:
#             return 1
#         else:
#             return value % sum1 
# print(minimum_steps([8,9,10,4,2], 23))

# def sum_str(a, b):
#     return str((int(a or 0) + int(b or 0)))
# print(sum_str("4",""))

# def correct(string):
#     str1 = string.replace("5","S").replace("0","O").replace("1","I")
#     return str1
# print(correct("BUDAPE5T"))

# def bool_to_word(boolean):
#     if boolean == True:
#         return 'Yes'
#     else:
#         return 'No'
# print(bool_to_word(False))

# def adjacent_element_product(array):
#     return max(a*b for a,b in zip(array,array[1:]))
# print(adjacent_element_product([5, 1, 2, 3, 1, 4]))

# def adjacent_element_product(array):
#     return max(array[i]*array[i+1] for i in range(len(array)-1))
# print(adjacent_element_product([5, 1, 2, 3, 1, 4]))


# def string_to_array(s):
#     return [','.join(s.split(" "))]
# print(string_to_array("Basic tests"))

# def string_to_array(s):
#     return s.split(" ")
# print(string_to_array("I love arrays they are my favorite"))


#弧线长度是1/4周长，周长是2*pi*r
# import math
# def square_area(A):
#     r = (A / (0.5 * math.pi)) ** 2 
#     return round(r,2)
# print(square_area(100))

# def derive(coefficient, exponent): 
#     return str(coefficient*exponent)+'x^'+str(exponent-1)
# print(derive(7,8))

# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     if distance_to_pump > mpg * fuel_left:
#         return False
#     else:
#         return True
# print(zero_fuel(50, 25, 2))

# def difference_in_ages(ages):
#     return(min(ages),max(ages),max(ages)-min(ages))
# print(difference_in_ages([5, 8, 72, 98, 41, 16, 55]))

# def triple_trouble(one, two, three):
#     return ''.join(''.join(a) for a in zip(one,two,three))
# print(triple_trouble("LLh", "euo", "xtr"))

# def reverseWords(s):
#     alist = s.split(' ')[::-1]
#     return ' '.join(alist)
# print(reverseWords('The greatest victory is that which requires no battle'))

# def between(a,b):
#     alist = []
#     for i in range(a,b+1,1):
#         alist.append(i)
#     return alist
# print(between(-1,4))

# def well(x):
#     badcount = x.count('bad')
#     goodcount = x.count('good')
#     if goodcount == 0:
#         return 'Fail!'
#     elif goodcount <= 1 and goodcount > 0:
#         return 'Publish!'
#     elif goodcount >=2:
#         return 'I smell a series!'
# print(well([ 'bad', 'bad', 'bad', 'bad']))

# def how_much_i_love_you(nb_petals):
#     dict1 = {1:'I love you',2:'a little',3:'a lot',4:'passionately',5:'madly',6:'not at all'}
#     return dict1[nb_petals % 6]
# print(how_much_i_love_you(7)


# age = input('age: ')
# if int(age) >= 18:
#     print('qiqi,happy 18th birthday')
# else:
#     print('qiqi,happy '+age +'th' +' birthday')

# def bin_to_decimal(inp):
#     return int(inp,2)
# print(bin_to_decimal("1"))

# def nth_even(n):
#     return (n * 2) -2
# print(nth_even(1298734))

# import math
# def nearest_sq(n):
#     return round(math.sqrt(n)) ** 2
# print(nearest_sq(10))

# def bmi(weight, height):
#     bmi = weight / (height ** 2)
#     if bmi <= 18.5:
#         return "Underweight"
#     elif bmi > 18.5 and bmi <= 25.0:
#         return "Normal"
#     elif bmi > 25.0 and bmi <= 30.0:
#         return "Overweight"
#     else:
#         return 'Obese'
# print(bmi(80, 1.80))


# def remove_exclamation_marks(s):
#     return s.replace('!','')
# print(remove_exclamation_marks('Oh, no!!!')

# def solve(s):
#     uppercount = lowercount = digitcount = charactercount = 0
#     for i in s:
#         if i.isupper():
#             uppercount += 1
#         elif i.islower():
#             lowercount += 1
#         elif i.isdigit():
#             digitcount += 1
#         else:
#             charactercount += 1
#     return [uppercount,lowercount,digitcount,charactercount]
# print(solve("@mw>0=QD-iAx!rp9TaG?o&M%l$34L.nbft"))

# def triangular(n):
#     if n <= 0:
#         return 0
#     else:
#         sum = 0
#         for i in range(1,n+1):
#             sum += i
#         return sum
# print(triangular(2))
# def triangular(n):
#     if n > 0:
#         return n * (n + 1) // 2
#     else:
#         return 0
# print(triangular(9))

#数学忘光光了 累加可以用等差数列求和公式来实现 我竟然还用的for循环

# 只能通过第一个元素+另一个元素=target的情况
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for i in nums:
#             chazhi = target - i
#             if chazhi in nums:
#                 return [nums.index(i),nums.index(chazhi)]
# s = Solution()
# print(s.twoSum([2,4,3],6))

#执行最后几个测试用例时超时：
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]
#         return []
# s = Solution()
# print(s.twoSum([3,2,4],8))

# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """

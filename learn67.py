'''
For a given string s find the character c (or C) with longest consecutive repetition and return:
(c, l)
where l (or L) is the length of the repetition. If there are two or more characters with the same l return the first in order of appearance.
For empty string return:
('', 0)
Happy coding! :)
对于给定的字符串s，找到具有最长连续重复的字符c（或C）并返回：
（c，l）
其中l（或L）是重复的长度。 如果有两个或多个相同的字符l按出现顺序返回第一个。
对于空字符串返回：
（''，0）
编码愉快！ :)
'''
# 1.
# def longest_repetition(chars):
#     if len(chars) == 0 or len(chars) == 1:
#         return(chars,len(chars))
#     result = [1] * len(chars)
#     for left in range(len(chars)-1):
#         for right in range(left+1,len(chars)):
#             if chars[left] == chars[right]:
#                 result[left] += 1
#             else:
#                 break
#     return (chars[result.index(max(result))],max(result))
# print(longest_repetition("aaaabb"))
# print(longest_repetition(''))
# print(longest_repetition('a'))
# print(longest_repetition("bbbaaabaaaa"))
# print(longest_repetition("cbdeuuu900"))
# print(longest_repetition("abbbbb"))
# print(longest_repetition("aabb"))

# 2.
# def longest_repetition(chars):
#     max_char,max_count = '',0
#     char,count = '',0
#     for c in chars:
#         if c != char:
#             count,char = 0,c
#         count += 1
#         if count > max_count:
#             max_char,max_count = char,count
#     return max_char,max_count
# print(longest_repetition("aaaaaab")) 
# print(longest_repetition("b")) 
# print(longest_repetition('cbdeuuu900'))
# print(longest_repetition('abbbbb'))

# 3.
# from itertools import groupby
# def longest_repetition(chars):
#     return max(((char,len(list(group)))for char,group in groupby(chars)),
#            key=lambda char_group: char_group[1],default=("",0))
# print(longest_repetition('abbbbb'))
# print(longest_repetition("b"))
# print(longest_repetition(""))
# print(longest_repetition('abac'))

# 4.
# import re
# def longest_repetition(chars):
#     if not chars:
#         return ('',0)
#     longest = max(re.findall(r"((.)\2*)",chars),key=lambda x: len(x[0]))
#     return (longest[1],len(longest[0]))
# print(longest_repetition('abac'))
# print(longest_repetition(""))
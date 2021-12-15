'''
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.
Notes:
Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered
Input strings s1 and s2 are null terminated.
Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
完成函数scramble（str1，str2），如果可以重新排列一部分str1字符以匹配str2，则返回true，否则返回false。
笔记：
仅使用小写字母（a-z）。 不包含标点符号或数字。
性能需要考虑
输入字符串s1和s2为空终止。
'''
# def scramble(s1, s2):
#     s2 = list(set(s2))
#     s1 = list(set(s1))
#     print(s1,s2)
#     for i in s2:
#         if i not in s1:
#             return False
#             break
#         else:
#             return True
# print(scramble('katas', 'steak')) 


# def scramble(s1, s2):
    # for i in set(s2):
        # if s1.count(i) < s2.count(i):
            # return False
    # return True
# print(scramble('cedewaraaossoqqyt', 'codewars')) 

# 高赞
from collections import Counter
def scramble(s1,s2):
    return len(Counter(s2) - Counter(s1)) == 0
print(scramble('cedewaraaossoqqyt', 'codewars')) 
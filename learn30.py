'''
Given a string of words, you need to find the highest scoring word.
Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
You need to return the highest scoring word as a string.
If two words score the same, return the word that appears earliest in the original string.
All letters will be lowercase and all inputs will be valid.
给定一串单词，您需要找到得分最高的单词。
一个单词的每个字母都根据其在字母表中的位置进行评分：a = 1，b = 2，c = 3，依此类推。
您需要将得分最高的单词作为字符串返回。
如果两个单词得分相同，则返回最早出现在原始字符串中的单词。
所有字母均为小写，所有输入均有效。
test.assert_equals(high('man i need a taxi up to ubud'), 'taxi')
test.assert_equals(high('what time are we climbing up the volcano'), 'volcano')
test.assert_equals(high('take me to semynak'), 'semynak')
'''
# ord()函数的作用是：获取字符对应的ASCII数值
# 几个常见字母的ASCII码大小： “A”为65；“a”为97；“0”为 48

# def high(x):
#     alist = []
#     for i in x.lower().split(' '):
#         # print(i)
#         b = 0
#         for j in i:
#             # print(j)
#             b += ord(j) - ord('a') + 1
#         alist.append(b)
#         # print(alist)  
#     return x.split(' ')[alist.index(max(alist))]
# print(high('man i need a taxi up to ubud'))

# 高赞
def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
print(high('man i need a taxi up to ubud'))
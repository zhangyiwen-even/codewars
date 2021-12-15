'''
Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types.
简单，给定一个字符串，返回最短单词的长度。
字符串永远不会为空，您无需考虑其他数据类型。
'''

def find_short(s):
    b = s.split(' ')
    # print(b)
    return min(len(i) for i in b)        
print(find_short("Lets all go on holiday somewhere very cold"))
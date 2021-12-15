'''
An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
Implement a function that determines whether a string that contains only letters is an isogram. 
Assume the empty string is an isogram. Ignore letter case.
等距图是一个没有重复字母，连续或不连续的单词。 
实现一个函数，该函数确定仅包含字母的字符串是否为等距图。 假设空字符串是一个等轴测图。 忽略字母大小写。
'''
def is_isogram(string):
    str1 = string.lower()
    for i in range(len(str1)):
        if str1.count(str1[i]) != 1:
            return False
        else:
            return True

print(is_isogram('ASDA'))
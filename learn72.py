'''
You are given two arrays a1 and a2 of strings. Each string is composed with letters from a to z. 
Let x be any string in the first array and y be any string in the second array.
Find max(abs(length(x) − length(y)))
If a1 and/or a2 are empty return -1 in each language except in Haskell (F#)
where you will return Nothing (None).
Example:
a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
mxdiflg(a1, a2) --> 13
Bash note:
input : 2 strings with substrings separated by ,
output: number as a string
给您两个字符串数组a1和a2。 每个字符串由字母a到z组成。 令x为第一个数组中的任何字符串，y为第二个数组中的任何字符串。

求max（abs（length（x）− length（y）））

如果a1和/或a2为空，则除Haskell（F＃）以外的每种语言都返回-1，在Haskell（F＃）中，您将返回Nothing（无）。

例：
a1 = [“ hoqq”，“ bbllkw”，“ oox”，“ ejjuyyy”，“ plmiis”，“ xxxzgpsssa”，“ xxwwkktt”，“ znnnnfqknaz”，“ qqquuhii”，“ dvvvwz”]
a2 = [“ cccooommaaqqoxii”，“ gggqaffhhh”，“ tttoowwwmmww”]
mxdiflg（a1，a2）-> 13
重击笔记：
输入：2个字符串，其子字符串由，
输出：数字作为字符串
'''
# def mxdiflg(a1,a2):
#     if a1 and a2:
#         return max(abs(len(x) - len(y)) for x in a1 for y in a2)
#     return -1
# print(mxdiflg(["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"],
# ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]))

# def mxdiflg(a1,a2):
#     if a1 and a2:
#         return max(
#             len(max(a1,key=len)) - len(min(a2,key=len)),
#             len(max(a2,key=len)) - len(min(a1,key=len)))
#     return -1
# print(mxdiflg(["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"],
# ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]))

def mxdiflg(a1,a2):
    mx = -1
    for x in a1:
        for y in a2:
            diff = abs(len(x) - len(y))
            if (diff > mx):
                mx = diff
    return mx
print(mxdiflg(["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"],
["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]))
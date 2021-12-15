'''
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.
Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
Please note that using encode is considered cheating.
ROT13是一种简单的字母替换密码，它将字母中的字母替换为后面的13个字母。 ROT13是凯撒密码的一个示例。
创建一个接受字符串并返回用Rot13加密的字符串的函数。 如果字符串中包含数字或特殊字符，则应按原样返回它们。 像原来的Rot13“实现”一样，仅应转换来自拉丁语/英语字母的字母。
请注意，使用编码被认为是作弊行为。
'''
# ASCii的值加13，ascii转换为数值--ord函数，数值转为ascii--chr函数

# maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
# 两个字符串的长度必须相同，为一一对应的关系。
# 注：Python3.4 已经没有 string.maketrans() 了，取而代之的是内建函数: bytearray.maketrans()、bytes.maketrans()、str.maketrans() 。

# import string
# from codecs import encode as _dont_use_this_
# trans = str.maketrans('ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz','NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')
# def rot13(message):
#     return message.translate(trans)
# print(rot13('Test'))
# print(rot13('test'))

import string
from codecs import encode as _dont_use_this_
from string import lowercase,uppercase
def rot13(message):
    lower = str.maketrans(lowercase,lowercase[13:] + lowercase[:13])
    upper = str.maketrans(uppercase,uppercase[13:] + uppercase[13:])
    return message.translate(lower).translate(upper)
print(rot13('Test'))
print(rot13('test'))
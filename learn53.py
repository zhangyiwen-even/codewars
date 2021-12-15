'''
Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"
Your task is to process a string with "#" symbols.
Examples
"abc#d##c"      ==>  "ac"
"abc##d######"  ==>  ""
"#######"       ==>  ""
""              ==>  ""
'''

# def clean_string(s):
#     result = []
#     for i in s:
#         if i == '#':
#             if result:
#                 result.pop()
#         else:
#             result.append(i)
#     return ''.join(result)
# print(clean_string('abc#d##c'))

# 高赞
# re.sub(pattern, repl, string, count=0, flags=0)
# 对于输入的一个字符串，利用正则表达式（的强大的字符串处理功能），
# 去实现（相对复杂的）字符串替换处理，然后返回被替换后的字符串
# 共有五个参数。其中三个必选参数：pattern, repl, string,两个可选参数：count, flags

# 第一个参数：pattern,表示正则中的模式字符串。

# 第二个参数：repl，就是replacement，被替换的字符串的意思。repl可以是字符串，也可以是函数。
# 如果repl是字符串的话，其中的任何反斜杠转义字符，都会被处理的。
# 即：\n：会被处理为对应的换行符； \r：会被处理为回车符；
# 其他不能识别的转移字符，则只是被识别为普通的字符：
# 比如\j，会被处理为j这个字母本身；
# 反斜杠加g以及中括号内一个名字，即：\g，对应着命了名的组，named group

# 第三个参数：string，即表示要被处理，要被替换的那个string字符串。

# 第四个参数：count，对于匹配到的内容，只处理其中一部分。

# 第五个参数：flags

# re?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
# .	匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
import re
def clean_string(s):
    while '#' in s:
        s = re.sub('.?#','',s,count=1)
    return s
print(clean_string('abc#d##c'))
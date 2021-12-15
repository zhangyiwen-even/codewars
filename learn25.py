'''
You receive the name of a city as a string, and you need to return a string that shows how many times each letter shows up in the string by using an asterisk (*).
For example:
"Chicago"  -->  "c:**,h:*,i:*,a:*,g:*,o:*"
As you can see, the letter c is shown only once, but wih 2 asterisks.
The return string should include only the letters (not the dashes, spaces, apostrophes, etc). There should be no spaces in the output, and the different letters are separated by a comma (,) as seen in the example above.
Note that the return string must list the letters in order of their first appearence in the original string.
More examples:
"Bangkok"    -->  "b:*,a:*,n:*,g:*,k:**,o:*"
"Las Vegas"  -->  "l:*,a:**,s:**,v:*,e:*,g:*"
您将以字符串形式接收城市名称，并且需要返回一个字符串，该字符串通过使用星号（*）来显示每个字母出现在字符串中的次数。
例如：
“芝加哥”->“ c：**，h：*，i：*，a：*，g：*，o：*”
如您所见，字母c仅显示一次，但带有2个星号。
返回字符串应仅包含字母（不包括破折号，空格，撇号等）。 如上例所示，输出中不应包含空格，并且不同的字母之间用逗号（，）分隔。
请注意，返回字符串必须按字母在原始字符串中的首次出现顺序列出。
'''
# 输出为字典 且为数字 而不是*
# def get_strings(city):
#     alist = list(city.lower())
#     dict1 = {}
#     # print(alist)
#     for i in alist:
#         if i in dict1:
#             dict1[i] += 1
#         else:
#             dict1[i] = 1
#     print(dict1)
# get_strings('Bangkok')

# 高赞
# from collections import Counter

# def get_strings(city):
#     return ",".join(f"{char}:{'*'*count}" for char,count in Counter(city.replace(" ","").lower()).items())
# print(get_strings('Bangkok'))

def get_strings(city):
    city = city.lower()
    result = ""
    for i in city:
        if i in result:
            pass
        elif i == " ":
            pass
        else:
            result += i + ":" + ("*" *city.count(i)) + ","
    return result[:-1]
print(get_strings('Bangkok'))
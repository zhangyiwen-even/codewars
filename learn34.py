'''
Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings. All words must have their first letter capitalized without spaces.
For instance:
camelcase("hello case") => HelloCase
camelcase("camel case word") => CamelCaseWord
Don't forget to rate this kata! Thanks :)
为字符串编写简单的.camelCase方法（PHP中的camel_case函数，C＃中的CamelCase或Java中的camelCase）。 所有单词的首字母必须大写，且不能有空格。
'''
# 自己
# def camel_case(string):
#     string = string.split(' ')
#     alist = []
#     for i in string:
#         alist.append(i.capitalize())
#     return ''.join(alist)
# print(camel_case('camel case word'))

# 高赞
def camel_case(string):
    return string.title().replace(' ','')
print(camel_case('camel case word'))
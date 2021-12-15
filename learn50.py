'''
When we attended middle school were asked to simplify mathematical expressions like "3x-yx+2xy-x" (or usually bigger), and that was easy-peasy ("2x+xy"). But tell that to your pc and we'll see!
Write a function: simplify, that takes a string in input, representing a multilinear non-constant polynomial in integers coefficients (like "3x-zx+2xy-x"), and returns another string as output where the same expression has been simplified in the following way ( -> means application of simplify):
All possible sums and subtraction of equivalent monomials ("xy==yx") has been done, e.g.:
"cb+cba" -> "bc+abc", "2xy-yx" -> "xy", "-a+5ab+3a-c-2a" -> "-c+5ab"
All monomials appears in order of increasing number of variables, e.g.:
"-abc+3a+2ac" -> "3a+2ac-abc", "xyz-xz" -> "-xz+xyz"
If two monomials have the same number of variables, they appears in lexicographic order, e.g.:
"a+ca-ab" -> "a-ab+ac", "xzy+zby" ->"byz+xyz"
There is no leading + sign if the first coefficient is positive, e.g.:
"-y+x" -> "x-y", but no restrictions for -: "y-x" ->"-x+y"
当我们上初中时，被要求简化数学表达式，例如“ 3x-yx + 2xy-x”（或通常更大），这很容易实现（“ 2x + xy”）。但是告诉您您的电脑，我们会看到的！
编写一个函数：simple，在输入中使用一个字符串，表示一个整数系数的多线性非常数多项式（例如“ 3x-zx + 2xy-x”），然后返回另一个字符串作为输出，其中相同的表达式已简化为以下方式（->表示简化的应用）：
已完成等效单项式（“ xy == yx”）的所有可能的加和减，例如：
“ cb + cba”->“ bc + abc”，“ 2xy-yx”->“ xy”，“ -a + 5ab + 3a-c-2a”->“ -c + 5ab”
所有单项式出现的顺序是变量数量的增加顺序，例如：
“ -abc + 3a + 2ac”->“ 3a + 2ac-abc”，“ xyz-xz”->“ -xz + xyz”
如果两个单项式具有相同数量的变量，则它们按字典顺序显示，例如：
“ a + ca-ab”->“ a-ab + ac”，“ xzy + zby”->“ byz + xyz”
如果第一个系数为正，则没有前导+号，例如：
“ -y + x”->“ x-y”，但不限制-：“ y-x”->“-x + y”
'''
# Python 的 re 模块提供了re.sub用于替换字符串中的匹配项。
# 语法：
# re.sub(pattern, repl, string, count=0, flags=0)
# 参数：
# pattern : 正则中的模式字符串。
# repl : 替换的字符串，也可为一个函数。
# string : 要被查找替换的原始字符串。
# count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。

# import re
# def simplify(poly):
#     pattern = re.compile(r'(?<=[a-z])(?=[\+\-])|(?<=[\+\-])(?=[a-z])|(?<=[0-9])(?=[a-z])')
#     poly = re.sub(pattern, ' ', poly)
#     cut = re.split(' ', poly)
#     dic = {}
#     for i in range(len(cut)):
#         if not cut[i].isalpha():
#             if cut[i] == '+':
#                 cut[i] = 1
#             elif cut[i] == '-':
#                 cut[i] = -1
#             else:
#                 cut[i] = int(cut[i])
#         else:
#             cut[i] = ''.join(sorted(cut[i]))
#             if cut[i] not in dic:
#                 if i == 0:
#                     dic[cut[i]] = 1
#                 else:
#                     dic[cut[i]] = cut[i-1]
#             else:
#                 dic[cut[i]] += cut[i-1]
#     list1 = sorted(dic.items(), key=lambda x: (len(x[0]), x[0]))
#     res = ''
#     for each in list1:
#         if each[1] == -1:
#             res += '-' + each[0]
#         elif each[1] == 0:
#             pass
#         elif each[1] == 1:
#             res += '+' + each[0]
#         elif each[1] > 1:
#             res += '+' + str(each[1]) + each[0]
#         else:
#             res += str(each[1]) + each[0]
#     return res.strip('+')

# 高赞
# import re
# def simplify(poly):
#     # 获得每个术语的3个部分（即使不存在）：（+/-，系数，变量）
#     # [...]	用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
#     # \d	匹配任意数字，等价于 [0-9].
#     # [a-z]	匹配任何小写字母
#     # re*	匹配0个或多个的表达式。
#     # re+	匹配1个或多个的表达式。
#     # findall 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
#     matches = re.findall(r'([+\-]?)(\d*)([a-z]+)',poly)
#     # 获取系数（包括符号）和排序变量（供以后比较）的int等效项
#     expanded = [[int(i[0] + (i[1] if i[1] != "" else "1")),''.join(sorted(i[2]))] for i in matches]
#     # 从上面的列表中获取唯一变量。 首先按长度排序，然后按字母顺序排序
#     variables = sorted(list(set(i[1] for i in expanded)),key=lambda x: (len(x),x))
#     # 获取每个变量的系数总和（位于扩展中）
#     coefficients = {v:sum(i[0] for i in expanded if i[1] == v) for v in variables}
#     # 将它们加上+号，删除"1"系数，并将"+-"更改为"-"
#     return '+'.join(str(coefficients[v]) + v for v in variables if coefficients[v] !=0).replace('1','').replace('+-','-')
# print(simplify('-a + 5ab + 3a-c-2a'))

# 高赞
# Python 字典(Dictionary) get() 函数返回指定键的值，如果值不在字典中返回默认值。
# get()方法语法： dict.get(key, default=None)
# key -- 字典中要查找的键。
# default -- 如果指定键的值不存在时，返回该默认值。

# import re
# def simplify(poly):
#     terms = {}
#     for sign,coef,vars in re.findall(r'([+\-]?)(\d*)([a-z]*)',poly):
#         sign = (-1 if sign == '-' else 1)
#         coef = sign * int(coef or 1)
#         vars = ''.join(sorted(vars))
#         terms[vars] = terms.get(vars,0) + coef
#     terms = sorted(terms.items(), key=lambda vars: (len(vars), vars))
#     return ''.join(map(format_term,terms)).strip('+')
#     # print(terms)

# def format_term(vars,coef):
#     if coef == 0:
#         return ''
#     if coef == 1:
#         return '+' + vars
#     if coef == -1:
#         return '-' + vars
#     return '%+i%s' %(coef,vars)
# print(simplify('-a+5ab+3a-c-2a'))
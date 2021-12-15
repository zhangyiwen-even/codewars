'''
Given a mathematical equation that has *,+,-,/, reverse it as follows:
solve("100*b/y") = "y/b*100"
solve("a+b-c/d*30") = "30*d/c-b+a"
'''
# 正则表达式中\W+表示匹配包括下划线的任何单词字符。
# import re
# def solve(eq):
    # return ''.join(reversed(re.split(r'(\W+)',eq)))
# print(solve("100*b/y"))
    
# def solve(eq):
#     leq = (
#         eq.replace('*',' * ')
#         .replace('/',' / ')
#         .replace('+',' + ')
#         .replace('-',' - ')
#         .split(' ')
#     )

#     out = ''.join(leq[::-1])
#     return out
# print(solve("100*b/y"))

# def solve(eq):
#     r = []
#     n = ""
#     for i in eq:
#         if i in "*/-+":
#             r.append(n)
#             r.append(i)
#             n = ""
#         else:
#             n += i
#     r.append(n)
#     r.reverse()
#     return "".join(r)
# print(solve("100*b/y"))

import re
def solve(eq):
    return "".join(re.split("([*/+-])",eq)[::-1])
print(solve("100*b/y"))
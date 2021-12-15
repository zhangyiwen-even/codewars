'''
Check to see if a string has the same amount of 'x's and 'o's.
The method must return a boolean and be case insensitive. 
The string can contain any char.
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
检查字符串是否具有相同数量的“ x”和“ o”。 
该方法必须返回一个布尔值并且不区分大小写。 该字符串可以包含任何字符。
'''
# def xo(s):
#     alist = list(s.lower())
#     xcount = ocount = 0
#     for i in alist:
#         if i == 'x':
#             xcount += 1
#         elif i == 'o':
#             ocount += 1
#     if xcount == ocount:
#         print('True')
#     else:
#         print('False')
# xo('ooxX111')
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')
xo('xxoooooo')

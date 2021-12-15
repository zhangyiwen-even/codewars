'''
In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, 
for the sake of simplicity, are named with letters from a to m.
The colors used by the printer are recorded in a control string. For example a "good" control string would be aaabbbbhaijjjm 
meaning that the printer used three times color a, four times color b, one time color h then one time color a...
Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced 
e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.
You have to write a function printer_error which given a string will output the error rate of the printer 
as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string.
Don't reduce this fraction to a simpler expression.
The string has a length greater or equal to one and contains only letters from a to z.
#Examples:
s="aaabbbbhaijjjm"
error_printer(s) => "0/14"
s="aaaxbbbbyyhwawiwjjjwwm"
error_printer(s) => "8/22"
在工厂中，打印机会打印盒子的标签。对于一种盒子，打印机必须使用以下颜色：
为了简单起见，以字母a到m命名。
打印机使用的颜色记录在控制字符串中。例如，“好”控制字符串将为aaabbbbhaijjjm
这意味着打印机使用了三种颜色a，四种颜色b，一种颜色h然后一种颜色a ...
有时会出现问题：颜色不足，技术故障以及产生“不良”控制字符串
例如aaaxbbbbyyhwawiwjjjwwm的字母不是从a到m。
您必须编写一个函数printer_error，给定一个字符串将输出打印机的错误率
作为表示有理数的字符串，其分子是错误数，而分母是控制字符串的长度。
不要将此分数简化为一个更简单的表达式。
字符串的长度大于或等于1，并且仅包含ato z的字母。
＃例子：
s =“ aaabbbbhaijjjm”
error_printer（s）=>“ 0/14”
s =“ aaaxbbbbyyhwawiwjjjwwm”
error_printer（s）=>“ 8/22”
'''
# def printer_error(s):
#     rlen=len(s)
#     alist = list(s)
#     ecount = 0
#     for i in alist:
#         if i != 'a' and i != 'b' and i != 'c' and i != 'd' and i != 'e' and i != 'f' and i != 'g' and i != 'h' and i != 'i' and i != 'j' and i != 'k' and i != 'l' and i != 'm':
#             ecount += 1
#             print(ecount/rlen)
# printer_error('aaabbbbhaijjjm')

#高赞1
# from re import sub
# def printer_error(s):
    # return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))
# print(printer_error('aaaxbbbbyyhwawiwjjjwwm'))
#高赞2
def printer_error(s):
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]),len(s))
print(printer_error('aaaxbbbbyyhwawiwjjjwwm'))
'''
Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
Write a function which takes a list of strings and returns each line prepended by the correct number.
The numbering starts at 1. The format is n: string. Notice the colon and space in between.
Examples:
number([]) # => []
number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]
您的团队正在编写一个精美的新文本编辑器，您的任务是实施行号。
编写一个函数，该函数接受字符串列表并返回以正确数字开头的每一行。
编号从1开始。格式为n：字符串。 注意之间的冒号和空格。
例子：
number（[]）＃=> []
number（[“ a”，“ b”，“ c”]）＃=> [“ 1：a”，“ 2：b”，“ 3：c”]
'''
# def number(lines):
    # return ['%d: %s' % v for v in enumerate(lines,1)]
# print(number(["a","b","c","z","y"]))

# def number(lines):
#     return ["{0}: {1}".format(i + 1,lines[i]) for i in range(len(lines))]
# print(number(["a","b","c"]))

# def number(lines):
#     return ['{}:{}'.format(n,s) for (n,s) in enumerate(lines,1)]
# print(number(["a","b","c"]))

# def number(lines):
    # return [str(x+1) + ": " + lines[x] for x in range(len(lines))]
# print(number(["a","b","c"]))

# def number(lines):
#     a = []
#     for i,c in enumerate(lines,1):
#         str_var = str(i) + ': ' + str(c)
#         a.append(str_var)
#     return a
# print(number(["a","b","c"]))
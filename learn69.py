'''
In this Kata, we are going to reverse a string while maintaining the spaces (if any) in their original place.
For example:
solve("our code") = "edo cruo"
-- Normal reversal without spaces is "edocruo". 
-- However, there is a space at index 3, so the string becomes "edo cruo"
solve("your code rocks") = "skco redo cruoy". 
solve("codewars") = "srawedoc"
More examples in the test cases. All input will be lower case letters and in some cases spaces.
'''
# python中next()返回迭代器的下一个项目
# next()函数要跟生成迭代器的iter()函数一起使用
# def solve(s):
#     it = reversed(s.replace(' ',''))
#     return ''.join(c if c == ' ' else next(it) for c in s)
# print(solve("our code"))

# def solve(s):
    # space_index = [i for i in range(len(s)) if s[i] == " "]
    # s = ''.join(s.split())
    # s = s[::-1]
    # for i in space_index:
        # s = s[:i] + " " + s[i:]
    # return s
# print(solve("our code"))
# print(solve("your code rocks"))

# def solve(s):
#     rev = list(s.replace(' ','')[::-1])
#     for index,item in enumerate(s):
#         if item == ' ':
#             rev.insert(index,item)
#     return ''.join(rev)
# print(solve("your code rocks"))

# def solve(s):
#     r = [a for a in s if a != ' ']
#     return ''.join(a if a == ' ' else r.pop() for a in s)
# print(solve("your code rocks"))
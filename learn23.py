'''
Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
'''
# def valid_parentheses(string):
#     str1 = list(string)
#     if str1.count('(') != str1.count(')'):
#         return False
#     elif str1[0] == '(':
#         return False
#     else:
#         return True
# print(valid_parentheses('hi())('))

#括号的平衡性，最内的括号一定时左右相邻且平衡的。
# def valid_parentheses(string):
#     while '{}' in string or '[]' in string or '()' in string:
#         string = string.replace('{}','').replace('[]','').replace('()','')
#     return string == ''
# print(valid_parentheses('hi()(())()()'))

# def valid_parentheses(string):
#     #设置字典
#     braces = {'(':')','[':']','{':'}'}
#     stack = []
#     for i in string:
#         if i in braces.keys():
#             stack.append(i)
#         else:
#             if len(stack) == 0 or braces[stack.pop()] != i:
#                 return False
#     return len(stack) == 0           
# print(valid_parentheses('hi()(())()()'))

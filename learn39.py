'''
You need to write regex that will validate a password to make sure it meets the following criteria:
At least six characters long
contains a lowercase letter
contains an uppercase letter
contains a number
Valid passwords will only be alphanumeric characters.
您需要编写用于验证密码的正则表达式，以确保其符合以下条件：
至少六个字符
包含小写字母
包含一个大写字母
包含一个数字
有效密码只能是字母数字字符。
from re import search
Test.describe("Basic tests")
Test.assert_equals(bool(search(regex, 'fjd3IR9')), True)
Test.assert_equals(bool(search(regex, 'ghdfj32')), False)
Test.assert_equals(bool(search(regex, 'DSJKHD23')), False)
Test.assert_equals(bool(search(regex, 'dsF43')), False)
Test.assert_equals(bool(search(regex, '4fdg5Fj3')), True)
Test.assert_equals(bool(search(regex, 'DHSJdhjsU')), False)
Test.assert_equals(bool(search(regex, 'fjd3IR9.;')), False)
Test.assert_equals(bool(search(regex, 'fjd3  IR9')), False)
Test.assert_equals(bool(search(regex, 'djI38D55')), True)
Test.assert_equals(bool(search(regex, 'a2.d412')), False)
Test.assert_equals(bool(search(regex, 'JHD5FJ53')), False)
Test.assert_equals(bool(search(regex, '!fdjn345')), False)
Test.assert_equals(bool(search(regex, 'jfkdfj3j')), False)
Test.assert_equals(bool(search(regex, '123')), False)
Test.assert_equals(bool(search(regex, 'abc')), False)
Test.assert_equals(bool(search(regex, '123abcABC')), True)
Test.assert_equals(bool(search(regex, 'ABC123abc')), True)
Test.assert_equals(bool(search(regex, 'Password123')), True)
'''

# 正则表达式
# r开始匹配 ^匹配字符串的开头 $	匹配字符串的结尾
# .	匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
# re*	匹配0个或多个的表达式。
# [0-9]	匹配任何数字。类似于 [0123456789]
# [a-z]	匹配任何小写字母
# [A-Z]	匹配任何大写字母
# [a-zA-Z0-9]	匹配任何字母及数字
# (re)	对正则表达式分组并记住匹配的文本
# (?= re)	前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。
# 但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。
# (?=.*[A-Z])至少一个大写字母

# from re import search
# s = 'Password123'
# regex=r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])[a-zA-Z0-9]{6,}$"
# res = search(regex,s)
# print(res)


# verbose=FALSE，意思就是设置运行的时候不显示详细信息
#高赞 
# from re import compile,VERBOSE
# regex = compile("""
# ^                  # begin word
# (?=.*?[a-z])       # at least one lowercase letter 
# (?=.*?[A-Z])       # at least one uppercase letter
# (?=.*?[0-9])       # at least one number
# [A-Za-z\d]         # only alphanumeric
# {6,}               # at least 6 character long
# $                  # end word
# """,VERBOSE)
'''
Find the longest substring in alphabetical order.
Example: the longest alphabetical substring in "asdfaaaabbbbcttavvfffffdf" is "aaaabbbbctt".
There are tests with strings up to 10 000 characters long so your code will need to be efficient.
The input will only consist of lowercase characters and will be at least one letter long.
If there are multiple solutions, return the one that appears first.
Good luck :)
Test.assert_equals(longest('asd'), 'as')
Test.assert_equals(longest('nab'), 'ab')
Test.assert_equals(longest('abcdeapbcdef'), 'abcde')
Test.assert_equals(longest('asdfaaaabbbbcttavvfffffdf'), 'aaaabbbbctt')
Test.assert_equals(longest('asdfbyfgiklag'), 'fgikl')
Test.assert_equals(longest('z'), 'z')
Test.assert_equals(longest('zyba'), 'z')
按字母顺序找到最长的子字符串。
示例：“ asdfaaaabbbbcttavvfffffdf”中最长的字母子字符串为“ aaaabbbbctt”。
有些测试的字符串最长为10000个字符，因此您的代码将需要高效。
输入将仅包含小写字符，并且至少为一个字母长。
如果有多个解决方案，请返回最先出现的解决方案。
祝好运 ：）
'''
# 高赞1
# import re
# reg = re.compile('a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*')

# def longest(s):
#     return max(reg.findall(s),key=len)

# print(longest('zyba'))

# 高赞2
# import re
# def longest(s):
#     return max(re.findall(r'a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*',s),key=len)
# print(longest('nab'))

# 高赞3

# group（）在正则表达式中用于获取分段截获的字符串，解释如下代码（代码来自网络）：

# import re
# a = "123abc456"
# print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(0)    #123abc456,返回整体
# print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(1)    #123
# print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(2)    #abc
# print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(3)    #456

# 可以看出，正则表达式按照数字-字母-数字的顺序来获取相应字符串，那么分别就是“数字（group（1））--字母（group（2））--数字（group（3））”的对应关系，

# 其中，group（0）和group（）效果相同，均为获取取得的字符串整体。

# def longest(s):


words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
from collections import Counter
word_counts = Counter(words)
# 出现频率最高的3个单词
top_three = word_counts.most_common(1)
print(top_three)
'''
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!
Here's the deal:
It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
市场营销团队花费太多时间输入标签。
让我们用我们自己的标签生成器帮助他们！
这是交易：
它必须以井号（＃）开头。
所有单词的首字母必须大写。
如果最终结果超过140个字符，则必须返回false。
如果输入或结果为空字符串，则必须返回false。
Test.assert_equals(generate_hashtag(''), False, 'Expected an empty string to return False')
Test.assert_equals(generate_hashtag('Do We have A Hashtag')[0], '#', 'Expeted a Hashtag (#) at the beginning.')
Test.assert_equals(generate_hashtag('Codewars'), '#Codewars', 'Should handle a single word.')
Test.assert_equals(generate_hashtag('Codewars      '), '#Codewars', 'Should handle trailing whitespace.')
Test.assert_equals(generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice', 'Should remove spaces.')
Test.assert_equals(generate_hashtag('codewars is nice'), '#CodewarsIsNice', 'Should capitalize first letters of words.')
Test.assert_equals(generate_hashtag('CodeWars is nice'), '#CodewarsIsNice', 'Should capitalize all letters of words - all lower case but the first.')
Test.assert_equals(generate_hashtag('c i n'), '#CIN', 'Should capitalize first letters of words even when single letters.')
Test.assert_equals(generate_hashtag('codewars  is  nice'), '#CodewarsIsNice', 'Should deal with unnecessary middle spaces.')
Test.assert_equals(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'), False, 'Should return False if the final word is longer than 140 chars.')
'''

# def generate_hashtag(s):
#     str1 = '#'
#     if s == '' or len(s) >= 140:
#         return False
#     else:
#         t1 = s.title()
#         t2 = "".join(t1.split())
#         return str1 + t2
# print(generate_hashtag('Codewars     '))

# 高赞
# def generate_hashtag(s):
#     output = '#'
#     for word in s.split():
#         output += word.capitalize()
#     return False if (len(s) == 0 or len(output) > 140) else output
# print(generate_hashtag('Codewars     '))

# def generate_hashtag(s):
#     ans = '#' + str(s.title().replace(' ',''))
#     return ans and not len(ans) > 140 and ans or False
# print(generate_hashtag('Codewars     '))
'''
In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.
Examples:
"one" => 1
"twenty" => 20
"two hundred forty-six" => 246
"seven hundred eighty-three thousand nine hundred and nineteen" => 783919
Additional Notes:
The minimum number is "zero" (inclusively)
The maximum number, which must be supported is 1 million (inclusively)
The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
All tested numbers are valid, you don't need to validate them
'''


# import re
# def parse_int(string):
#     dict1 = {
#         'zero':0,
#         'one':1,
#         'two':2,
#         'three':3,
#         'four':4,
#         'five':5,
#         'six':6,
#         'seven':7,
#         'eight':8,
#         'nine':9,
#         'ten':10,
#         'eleven':11,
#         'twelve':12,
#         'thirteen':13,
#         'fourteen':14,
#         'fifteen':15,
#         'sixteen':16,
#         'seventeen':17,
#         'eighteen':18,
#         'nineteen':19,
#         'twenty':20,
#         'thirty':30,
#         'forty':40,
#         'fifty':50,
#         'sixty':60,
#         'seventy':70,
#         'eighty':80,
#         'ninety':90,
#     }
#     return 


# 高赞1
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
# enumerate(sequence, [start=0])
# sequence -- 一个序列、迭代器或其他支持迭代对象。
# start -- 下标起始位置。

# # 字典生成式
# words = {w:n for n,w in enumerate('zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split())}
# # 下标从2开始，2*10
# words.update({w: 10*n for n,w in enumerate('twenty thirty forty fifty sixty seventy eighty ninety hundred'.split(),2)})
# thousands = {w: 1000**n for n,w in enumerate('thousand million billion trillion quadrillion quintillion sextillion septillion octillion nonillion decillion'.split(),1)}

# def parse_int(string):
#     num = group = 0
#     for w in string.replace(' and ',' ').replace('-',' ').split():
#         if w == 'hundred':
#             group *= words[w]
#         elif w in words:
#             group += words[w]
#         else:
#             num += group * thousands[w]
#             group = 0
#     return num + group
# print(parse_int('seven hundred eighty-three thousand nine hundred and nineteen'))
# print(parse_int('twenty'))

# 高赞2
ONES = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
TENS = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

def parse_int(string):
    # print(string)
    numbers = []
    for token in string.replace('-',' ').split(' '):
        if token in ONES:
            numbers.append(ONES.index(token))
        elif token in TENS:
            numbers.append((TENS.index(token) + 2) * 10)
        elif token == 'hundred':
            numbers[-1] *= 100
        elif token == 'thousand':
            numbers = [x * 1000 for x in numbers]
        elif token == 'million':
            numbers = [x * 1000000 for x in numbers]
    return sum(numbers)
print(parse_int('seven hundred eighty-three thousand nine hundred and nineteen'))
print(parse_int('twenty'))
print(parse_int('two hundred forty-six'))
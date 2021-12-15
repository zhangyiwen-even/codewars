'''
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
将每个单词的第一个字母移到单词的末尾，然后在单词的末尾添加“ay”。 标点符号保持不变。
'''
#自己
# import string
# def pig_it(text):
#     #判断是否为标点符号
#     punc = string.punctuation
#     alist = []
#     text = text.split(' ')
#     for i in text:
#         if i in punc:
#             alist.append(i)
#         else:
#             alist.append(i[1:]+i[0]+'ay')
#     return(' '.join(alist))
# print(pig_it('Pig latin is cool !'))

#高赞
def pig_it(text):
    lst = text.split()
    return ' '.join([word[1:] + word[:1] +'ay' if word.isalpha() else word for word in lst])
print(pig_it('Pig latin is cool !'))
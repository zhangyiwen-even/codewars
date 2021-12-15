'''
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:
'abba' & 'baab' == true
'abba' & 'bbaa' == true
'abba' & 'abbba' == false
'abba' & 'abca' == false
Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:
anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
什么是字谜？ 好吧，如果两个单词都包含相同的字母，则它们是彼此的字谜。 例如：
编写一个函数，该函数将从列表中查找单词的所有字谜。 您将获得两个输入一个单词和一个带有单词的数组。
您应该返回所有字谜的数组，如果没有，则返回一个空数组。
'''
def anagrams(word, words):
    alist = []
    # words = set(words)
    for i in words:
        if sorted(word) == sorted(i):
            alist.append(i)
    return alist
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))

# 高赞 
# def anagrams(word, words):
#     return [i for i in words if sorted(i) == sorted(word)]
# print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
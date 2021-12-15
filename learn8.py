'''
Write a function that takes in a string of one or more words, and returns the same string, 
but with all five or more letter words reversed (Just like the name of this Kata). 
Strings passed in will consist of only letters and spaces. 
Spaces will be included only when more than one word is present.
Examples: spinWords( "Hey fellow warriors" ) => 
returns "Hey wollef sroirraw" spinWords( "This is a test") =>
returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"
编写一个函数，该函数接受一个或多个单词的字符串，并返回相同的字符串，但所有五个或多个字母单词都反转了（就像此Kata的名称一样）。 
传入的字符串将仅包含字母和空格。 仅当存在多个单词时才包含空格。
'''
def spin_words(sentence):
    a = sentence.split(' ') 
    list1 = list2 = []
    for i in a:
        if len(i) > 5:
            i = i[::-1]
            list1.append(i)
            # print(list1)
        #print(''.join(i))
        else:
            list2.append(i)
            # print(list2)
    print(' '.join(list2))
spin_words('This is another test')
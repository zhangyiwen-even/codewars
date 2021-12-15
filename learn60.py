'''
Given a string "abc" and assuming that each letter in the string has a value equal to its position in the alphabet, our string will have a value of 1 + 2 + 3 = 6. This means that: a = 1, b = 2, c = 3 ....z = 26.
You will be given a list of strings and your task will be to return the values of the strings as explained above multiplied by the position of that string in the list. For our purpose, position begins with 1.
nameValue ["abc","abc abc"] should return [6,24] because of [ 6 * 1, 12 * 2 ]. Note how spaces are ignored.
"abc" has a value of 6, while "abc abc" has a value of 12. Now, the value at position 1 is multiplied by 1 while the value at position 2 is multiplied by 2.
Input will only contain lowercase characters and spaces.
Good luck!
If you like this Kata, please try:
String matchup
Consonant value
给定字符串“ abc”，并假设字符串中的每个字母的值都等于其在字母表中的位置，则我们的字符串的值将为1 + 2 + 3 =6。
这意味着：a = 1，b = 2，c = 3 .... z = 26。
您将得到一个字符串列表，您的任务将是返回如上所述的字符串值乘以该字符串在列表中的位置。 就我们的目的而言，排名从1开始。
由于[6 * 1、12 * 2]，nameValue [“ abc”，“ abc abc”]应该返回[6,24]。 注意如何忽略空格。
“ abc”的值为6，而“ abc abc”的值为12。现在，位置1的值乘以1，而位置2的值乘以2。
输入将仅包含小写字符和空格。
祝好运！
如果您喜欢这个Kata，请尝试：
字符串对决
辅音值
'''
# def name_value(my_list):
#     dict1 = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'10','k':'11','l':'12','m':'13',
#     'n':'14','o':'15','p':'16','q':'17','r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'}
#     alist = []
#     for i in my_list:
#         alist.append(i)
#     # return alist
#     blist = []
#     for i in alist:
#         for j in i.split:
#             blist.append(j)
#     return blist
# print(name_value(["abc","abc abc"]))

# def name_value(my_list):
    # return [i*sum(map(lambda c: [0,ord(c)-96][c.isalpha()],w.lower()))for i,w in enumerate(my_list,1)]
# print(name_value(["abc","abc abc"]))

# from string import ascii_lowercase as alphabet
# def name_value(my_list):
#     value_map = dict((letter,i) for i,letter in enumerate(alphabet,1))
#     return [i * sum(value_map.get(letter,0) for letter in name) for i,name in enumerate(my_list,1)]
# print(name_value(["abc","abc abc"]))

# def name_value(s):
#     return [sum(ord(c) - 96 for c in s[i] if c != ' ') * (i + 1) for i in range(0,len(s))]
# print(name_value(["abc","abc abc"]))

# ord函数可以将字符转化为你所需要的ASCII码,chr函数可以将0-255中的任一整数 转化为你所需要的字符。
# def name_value(mylist):
    # return [sum(ord(c) - 96 for c in word.replace(" ","")) * (i + 1) for i,word in enumerate(mylist)]
# print(name_value(["codewars","abc","xyz"]))
# print(name_value(["abc","abc","abc","abc"]))
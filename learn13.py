'''
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string.
The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
计算重复次数
编写一个函数，该函数将返回在输入字符串中多次出现的不区分大小写的字母字符和数字的计数。
可以假定输入字符串仅包含字母（大写和小写）和数字。
“ abcde”-> 0＃没有字符重复多次
“ aabbcde”-> 2＃'a'和'b'
“ aabBcde”-> 2＃'a'出现两次，'b'两次（`b`和'B`）
“不可分割性”-> 1＃'i'出现六次
“个性”-> 2＃“ i”出现7次，“ s”出现两次
“ aA11”-> 2＃'a'和'1'
“ ABBA”-> 2＃'A'和'B'分别出现两次
'''
def duplicate_count(text):
    alist = list(text.lower())
    dcount = []
    for i in alist:
        if alist.count(i) > 1:
            dcount.append(i)
    return(len(set(dcount)))
print(duplicate_count('AABB'))
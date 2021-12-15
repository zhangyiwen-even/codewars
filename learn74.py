'''
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
'''

# def positive_sum(arr):
#     alist = []
#     for i in arr:
#         if i > 0:
#             alist.append(i)
#     return sum(alist)
# print(positive_sum([1,2,3,4,-5]))

# def positive_sum(arr):
#     return sum(x for x in arr if x > 0)
# print(positive_sum([1,2,3,-4,-5]))

'''
Create a method is_uppercase() to see whether the string is ALL CAPS. For example:

is_uppercase("c") == False
is_uppercase("C") == True
is_uppercase("hello I AM DONALD") == False
is_uppercase("HELLO I AM DONALD") == True
is_uppercase("ACSKLDFJSgSKLDFJSKLDFJ") == False
is_uppercase("ACSKLDFJSGSKLDFJSKLDFJ") == True
'''

# def is_uppercase(inp):
#     INP = inp.upper()
#     return True if inp == INP else False
# print('C')

# def is_uppercase(inp):
#     for i in inp:
#         if i.islower():
#             return False
#     return True
# print(is_uppercase("LD"))

# def is_uppercase(inp):
#     return inp.upper() == inp
# print(is_uppercase("LD"))


'''
A hero is on his way to the castle to complete his mission. 
However, he's been told that the castle is surrounded with a couple 
of powerful dragons! each dragon takes 2 bullets to be defeated, 
our hero has no idea how many bullets he should carry.. 
Assuming he's gonna grab a specific given number of bullets 
and move forward to fight another specific given number of dragons, will he survive?
Return True if yes, False otherwise :)
'''

# def hero(bullets,dragons):
#     num = bullets / 2
#     if num >= dragons:
#         return True
#     else:
#         return False
# print(hero(1500,751))

def hero(bullets,dragons):
    return bullets >= dragons * 2
print(hero(1500,751)) 
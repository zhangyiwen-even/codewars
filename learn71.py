'''
Digital root is the recursive sum of all the digits in a number.
Given n, take the sum of the digits of n. 
If that value has more than one digit, 
continue reducing in this way until a single-digit number is produced. 
This is only applicable to the natural numbers.
Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
'''

# def digital_root(n):
    # return n if n < 10 else digital_root(sum(map(int,str(n)))) 
# print(digital_root(16))
# print(digital_root(493193))

# def digital_root(n):
#     return n%9 or n and 9
# print(digital_root(493193))

# def digital_root(n):
    # while n > 9:
        # n = sum(map(int,str(n)))
    # return n
# print(digital_root(493193))

# def digital_root(n):
    # root = 0
    # for d in str(n):
        # root += int(d)
    # if len(str(root)) > 1:
        # root = digital_root(root)
    # return root
# print(digital_root(493193))

# def digital_root(n):
    # while n >= 10:
        # n = sum(divmod(n,10))
    # return n
# print(digital_root(493193))
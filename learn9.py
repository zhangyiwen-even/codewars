'''
Write a function that takes an integer as input, 
and returns the number of bits that are equal to one in the binary representation of that number. 
You can guarantee that input is non-negative.
Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
编写一个函数，该函数以整数作为输入，并返回该数字的二进制表示形式中等于1的位数。 您可以保证输入为非负数。
示例：1234的二进制表示形式是10011010010，因此在这种情况下该函数应返回5
'''

def count_bits(n):
    a = bin(int(n))
    list1 = list(a)
    print(list1.count('1'))
count_bits('255')
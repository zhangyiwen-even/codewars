'''
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.
For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
[10, 343445353, 3453445, 3453545353453] should return 3453455.
创建一个函数，该函数在给定最小4个正整数的数组的情况下返回两个最低正数的和。 不会传递浮点数或非正整数。
例如，当像[19、5、42、2、77]这样传递数组时，输出应为7。
[10，343445353，3453445，3453545353453]应该返回3453455。
'''
#自己
# def sum_two_smallest_numbers(numbers):
#     min1 = min(numbers)
#     numbers.remove(min1)
#     min2= min(numbers)
#     sum1 = min1 + min2
#     return sum1
# print(sum_two_smallest_numbers([19,5,42,2,77]))

#高赞
# def sum_two_smallest_numbers(numbers):
#     return sum(sorted(numbers)[:2])
# print(sum_two_smallest_numbers([19,5,42,2,77]))

def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]
print(sum_two_smallest_numbers([19,5,42,2,77]))
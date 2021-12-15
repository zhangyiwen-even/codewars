'''
You must implement a function maxDiff that return the difference between the biggest and the smallest value in a list(lst) received as parameter.
The list(lst) contains integers, that means it may contain some negative numbers.
If the list is empty or contains a single element, return 0.
The list(lst) is not sorted.
maxDiff([1, 2, 3, 4]); //return 3, because 4 - 1 == 3
maxDiff([1, 2, 3, -4]); //return 7, because 3 - (-4) == 7
'''
# def max_diff(lst):
#     if len(lst) >= 2:
#         return(sorted(lst)[-1] - sorted(lst)[0])
#     elif len(lst) <= 1:
#         return 0
# print(max_diff([1,2,3,-4]))

def max_diff(lst):
    return max(lst) - min(lst) if lst else 0
print(max_diff([1,2,3,-4]))
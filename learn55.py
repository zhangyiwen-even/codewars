'''
It's the academic year's end, fateful moment of your school report. The averages must be calculated. All the students come to you and entreat you to calculate their average for them. Easy ! You just need to write a script.
Return the average of the given array rounded down to its nearest integer.
The array will never be empty.
求均值
'''
# def get_average(marks):
#      n = len(marks)
#      sum1 = sum(marks)
#      average1 = int(sum1/n)
#      return average1
# print(get_average([1,2,15,15,17,11,12,17,17,14,13,15,6,11,8,7]))

# def get_average(marks):
#     return sum(marks) // len(marks)
# print(get_average([1,2,15,15,17,11,12,17,17,14,13,15,6,11,8,7]))

'''
In this Kata, you will be given a string of numbers in sequence and your task will be to return the missing number. If there is no number missing or there is an error in the sequence, return -1.
For example:
missing("123567") = 4 
missing("899091939495") = 92
missing("9899101102") = 100
missing("599600601602") = -1 -- no number missing
missing("8990919395") = -1 -- error in sequence. Both 92 and 94 missing.
The sequence will always be in ascending order.
More examples in the test cases.
在此Kata中，将按顺序提供一串数字，而您的任务将是返回丢失的数字。 如果没有数字丢失或序列中有错误，则返回-1。
missing（“ 123567”）= 4
丢失（“ 899091939495”）= 92
丢失（“ 9899101102”）= 100
missing（“ 599600601602”）= -1- 无数字丢失
missing（“ 8990919395”）= -1- 顺序错误。 92和94都失踪了。
序列将始终按升序排列。
'''
'''
Friday 13th or Black Friday is considered as unlucky day. Calculate how many unlucky days are in the given year.
Find the number of Friday 13th in the given year.
Input: Year as an integer.
Output: Number of Black Fridays in the year as an integer.
Examples:
unluckyDays(2015) == 3
unluckyDays(1986) == 1
13日星期五或黑色星期五被视为不幸的日子。 计算给定年份中有多少不幸的日子。
查找给定年份的星期五13号。
输入：Year（整数）。
输出：一年中的黑色星期五的数量（整数）。
例子：
unluckyDays（2015）== 3
unluckyDays（1986）== 1
'''
# import datetime
# def unlucky_days(year):
#     sum = 0
#     for month in range(1,13):
#         date = datetime.datetime(year,month,13).strftime("%w")
#         if date == '5':
#             sum += 1
#     return sum
# print(unlucky_days(2015))
# print(unlucky_days(1986))

# from datetime import date
# def unlucky_days(year):
#     return sum(date(year,m,13).weekday() == 4 for m in range(1,13))
# print(unlucky_days(2015))
# print(unlucky_days(1986))

# from calendar import weekday
# def unlucky_days(year):
#     return sum(1 for i in range(1,13) if weekday(year,i,13) == 4)
# print(unlucky_days(2019))
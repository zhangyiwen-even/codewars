'''
Your task is to write a function which returns the sum of following series upto nth term(parameter).
Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
您的任务是编写一个函数，该函数返回以下系列的和直到n项（参数）。
系列：1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 + ...


1/0*3+1 + 1/1*3+1 + 1/2*3+1 +...
'''

# def series_sum(n):
#     sum1 = 0
#     for i in range(0,n):
#         sum1 += 1/(1+3*(float(i)))
#     return (round(sum1,2))
# print(series_sum(2))
        
#高赞
def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3*i + 1) for i in range(n)))
print(series_sum(3))
    
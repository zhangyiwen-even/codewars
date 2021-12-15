'''
鲍勃正在准备通过智商测试。 此测试中最常见的任务是找出给定数字中的哪个不同于其他数字。 
鲍勃（Bob）发现，一个数字通常在均匀性上与其他数字不同。 帮助Bob-检查他的答案，
他需要一个程序，该程序在给定的数字中找到一个均匀度不同的数字，并返回该数字的位置。
！ 请记住，您的任务是帮助Bob解决真正的IQ测试，这意味着元素的索引从1（而不是0）开始
iq_test（“ 2 4 7 8 10”）=> 3 //第三个数字为奇数，其余数字为偶数
iq_test（“ 1 2 1 1”）=> 2 //第二个数字为偶数，其余数字为奇数
Bob is preparing to pass IQ test. The most frequent task in this test is to find 
out which one of the given numbers differs from the others.
Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, 
he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.
! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)
'''
# def iq_test(numbers):
#     numbers = numbers.split()
#     alist = [int(i) % 2 == 0 for i in numbers]
#     if alist.count(True) == 1:
#         return(alist.count(True) + 1)
#     else:
#         return(alist.count(False) + 1)
# print(iq_test("1 2 1 1"))
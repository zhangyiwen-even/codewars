'''
Consider a sequence u where u is defined as follows:
The number u(0) = 1 is the first one in u.
For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
There are no other numbers in u.
Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]
1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...
Task:
Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered (with <) sequence u (so, there are no duplicates).
Example:
dbl_linear(10) should return 22
考虑一个序列u，其中u的定义如下：
u（0）= 1是u中的第一个数字。
对于u中的每个x，y = 2 * x + 1和z = 3 * x + 1也必须在u中。
你没有其他数字。
例如：u = [1、3、4、7、9、10、13、15、19、21、22、27，...]
1给出3和4，然后3给出7和10,4给出9和13，然后7给出15和22，依此类推...
任务：
给定参数n时，函数dbl_linear（或dblLinear ...）返回有序（具有<）的序列u的元素u（n）（因此，没有重复项）。
dbl_linear（10）应该返回22
'''


# def dbl_linear(n):
#     alist = [1]
#     for i in alist:
#         alist.append((2*i) + 1)
#         alist.append((3*i) + 1)
#         if len(alist) > n*10:
#             break
#     # return sorted(list(set(alist)))[n]
#     return list(set(sorted(alist)))[n]
# print(dbl_linear(10))

# 高赞deque模块是python标准库collections中的一项，
# 它提供了两端都可以操作的序列，这意味着，在序列的前后你都可以执行添加或删除操作。
from collections import deque
def dbl_linear(n):
    h = 1; cnt = 0; q2, q3 = deque([]),deque([])
    while True:
        if (cnt >= n):
            return h
        q2.append(2 * h + 1)
        q3.append(3 * h + 1)
        h = min(q2[0],q3[0])
        if h == q2[0]: h = q2.popleft()
        if h == q3[0]: h = q3.popleft()
        cnt += 1
print(dbl_linear(10))
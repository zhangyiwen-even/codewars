'''
Make a program that filters a list of strings and returns a list with only your friends name in it.
If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...
Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
i.e.
friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
编写一个过滤字符串列表并返回仅包含您的朋友姓名的列表的程序。
如果名称中恰好有4个字母，则可以确定它必须是您的朋友！ 否则，您可以确定他不是...
例如：输入= [“ Ryan”，“ Kieran”，“ Jason”，“ Yous”]，输出= [“ Ryan”，“ Yous”]
即
朋友[“ Ryan”，“ Kieran”，“ Mark”]`shouldBe` [“ Ryan”，“ Mark”]
'''
#自己写的
# def friend(x):
#     alist = []
#     for i in x:
#         if len(i) == 4:
#             alist.append(i)
#     # print(alist)
#     return alist
# friend(["Ryan", "Kieran", "Mark",])

#高赞，列表生成式
def friend(x):
    return [i for i in x if len(i) == 4]
print(friend(["Ryan", "Kieran", "Mark",]))

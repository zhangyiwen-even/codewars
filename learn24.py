# import random
# def fake_bin(x):
#     alist = list(x)
#     print(alist)
#     ran1 = random.randint(0,4)
#     ran2 = random.randint(5,9)
#     for i in alist:
#         # print(ran1,ran2)
#         if i == '0':
#             i == ran1
#         else:
#             i == ran2
#     return alist
# print(fake_bin('100111001111'))

def fake_bin(x):
    return ''.join( '0' if i < '5' else '1' for i in x)
print(fake_bin('1001114567891111'))
'''
Kevin is noticing his space run out! Write a function that removes the spaces from the values and returns an array 
showing the space decreasing. For example, running 
this function on the array ['i', 'have','no','space'] would produce ['i','ihave','ihaveno','ihavenospace'].
test.assert_equals(spacey(['kevin', 'has','no','space']), [ 'kevin', 'kevinhas', 'kevinhasno', 'kevinhasnospace'])
test.assert_equals(spacey(['this','cheese','has','no','holes']), ['this','thischeese','thischeesehas','thischeesehasno','thischeesehasnoholes'])
凯文注意到他的空间用完了！ 编写一个从值中删除空格并返回一个显示空格减少的数组的函数。 
例如，在数组['i'，'have'，'no'，'space']上运行此函数将产生['i'，'ihave'，'ihaveno'，'ihavenospace']。
'''
# accumulate()表示累加
# from itertools import accumulate
# def spacey(array):
#     return list(accumulate(array))
# print(spacey(['this','cheese','has','no','holes']))

# def spacey(array):
#     return [''.join(array[:i+1]) for i in range(len(array))]
# print(spacey(['this','cheese','has','no','holes']))

# def spacey(array):
#     return ["".join(array[:i]) for i,_ in enumerate(array,1)]
# print(spacey(['this','cheese','has','no','holes']))

# from itertools import accumulate
# def spacey(array):
#     return list(map("".join,accumulate(array)))
# print(spacey(['this','cheese','has','no','holes']))

def spacey(array):
    new_s = []
    s = ""
    for i in array:
        s += i
        new_s.append(s)
    return new_s
print(spacey(['i', 'have','no','space']))
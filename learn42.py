'''
Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:
12 ==> 21
513 ==> 531
2017 ==> 2071
nextBigger(num: 12)   // returns 21
nextBigger(num: 513)  // returns 531
nextBigger(num: 2017) // returns 2071
If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):
9 ==> -1
111 ==> -1
531 ==> -1
nextBigger(num: 9)   // returns nil
nextBigger(num: 111) // returns nil
nextBigger(num: 531) // returns nil
创建一个采用正整数并返回下一个较大数字的函数，该数字可以通过重新排列其数字来形成。 例如：
Test.assert_equals(next_bigger(12),21)
Test.assert_equals(next_bigger(513),531)
Test.assert_equals(next_bigger(2017),2071)
Test.assert_equals(next_bigger(414),441)
Test.assert_equals(next_bigger(144),414)
'''
# def next_bigger(n):
#     s = str(n)
#     S = list(s[:-1])
#     reserves = [s[-1]]
#     for i in range(len(S)-1,-1,-1):
#         for j in range(len(reserves)):
#             if int(S[i]) < int(reserves[j]):
#                 S[i],reserves[j] = reserves[j],S[i]
#                 news = S[:i+1]
#                 news.extend(reserves)
#                 N = "".join(news)
#                 return int(N)
#         reserves.append(S[i])
#     return -1

# 高赞
def next_bigger(n):
    s = list(str(n))
    for i in range(len(s)-2,-1,-1):
        if s[i] < s[i+1]:
            t = s[i:]
            m = min(filter(lambda x: x>t[0], t))
            t.remove(m)
            t.sort()
            s[i:] = [m] + t
            return int("".join(s))
    return -1
print(next_bigger(144))
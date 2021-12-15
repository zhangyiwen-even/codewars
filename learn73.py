'''
You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.
Example:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
n being the length of the string array, if n = 0 or k > n or k <= 0 return "".
Note
consecutive strings : follow one after another without an interruption
您将得到一个字符串数组（列表）字符串和一个整数k。 您的任务是返回由数组中的k个连续字符串组成的第一个最长字符串。
例：
longest_consec（[[zone]，“ abigail”，“ theta”，“ form”，“ libe”，“ zas”，“ theta”，“ abigail”]，2）->“ abigailtheta”
n是字符串数组的长度，如果n = 0或k> n或k <= 0，则返回“”。
注意
连续的字符串：连续不断地跟随
'''
# def longest_consec(strarr,k):
#     result = ""
#     if k > 0 and len(strarr) >= k:
#         for index in range(len(strarr) - k + 1):
#             s = ''.join(strarr[index:index+k])
#             if len(s) > len(result):
#                 result = s
#     return result
# print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2))

def longest_consec(strarr,k):
    return max(["".join(strarr[i:i+k]) for i in range(len(strarr)-k+1)],key=len) if strarr and 0 < k <= len(strarr) else ""
# print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2))
print(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"],2))
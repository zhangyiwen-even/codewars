'''
This time no story, no theory. The examples below show you how to write function accum:
Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
这次没有故事，没有理论。 下面的示例向您展示如何编写函数accum：
例子：
accum（“ abcd”）->“ A-Bb-Ccc-Dddd”
accum（“ RqaEzty”）->“ R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy”
accum（“ cwAt”）->“ C-Ww-Aaa-Tttt”
accum的参数是一个字符串，仅包含来自a..z和A..Z的字母。
'''
# enumerate函数 
# def accum(s):
#     return '-'.join(c.upper() + c.lower() * i for i,c in enumerate(s))
# print(accum("abcd"))

# def accum(s):
#     return '-'.join((a * i).title() for i,a in enumerate(s,1))
# print(accum("abcd"))

# def accum(s):
#     output = ""
#     for i in range(len(s)):
#         output += (s[i]*(i+1)) + '-'
#     return output.title()[:-1]
# print(accum("RqaEzty"))

# def accum(s):
#     blist = []
#     for i,j in enumerate(s):
#         blist.append(j.upper() + j.lower() * i)
#     return '-'.join(blist)
# print(accum("RqaEzty"))

'''
The first input array is the key to the correct answers to an exam, like ["a", "a", "b", "d"]. The second one contains a student's submitted answers.
The two arrays are not empty and are the same length. Return the score for this array of answers, giving +4 for each correct answer, 
-1 for each incorrect answer, and +0 for each blank answer, represented as an empty string (in C the space character is used).
If the score < 0, return 0.
For example:
checkExam(["a", "a", "b", "b"], ["a", "c", "b", "d"]) → 6
checkExam(["a", "a", "c", "b"], ["a", "a", "b",  ""]) → 7
checkExam(["a", "a", "b", "c"], ["a", "a", "b", "c"]) → 16
checkExam(["b", "c", "b", "a"], ["",  "a", "a", "c"]) → 0
第一个输入数组是正确答案的键，例如[“ a”，“ a”，“ b”，“ d”]。 第二个包含学生提交的答案。
这两个数组不为空，并且长度相同。 返回此答案数组的分数，每个正确答案给出+4，每个错误答案给出-1，每个空白答案给出+0，以空字符串表示（在C中使用空格字符）。
如果分数<0，则返回0。
例如：
checkExam（[“ a”，“ a”，“ b”，“ b”]，[“ a”，“ c”，“ b”，“ d”]）→6
checkExam（[“ a”，“ a”，“ c”，“ b”]，[“ a”，“ a”，“ b”，“”]）→7
checkExam（[“ a”，“ a”，“ b”，“ c”]，[“ a”，“ a”，“ b”，“ c”]）→16
checkExam（[“ b”，“ c”，“ b”，“ a”]，[“”，“ a”，“ a”，“ c”]）→0
'''

# def check_exam(arr1,arr2):
#     score = 0
#     for i in range(0,4):
#         if arr1[i] == arr2[i]:
#             score += 4
#         elif arr1[i] == "" or arr2[i] == "":
#             score += 0
#         else:
#             score -= 1
#     return score if score >= 0 else 0
# print(check_exam(["b", "c", "b", "a"], ["",  "a", "a", "c"]))

# def check_exam(arr1,arr2):
#     return max(0,sum(4 if a == b else -1 for a,b in zip(arr1,arr2) if b))
# print(check_exam(["b", "c", "b", "a"], ["",  "a", "a", "c"]))
# print(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]))
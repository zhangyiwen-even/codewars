'''
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. 
Any whitespace at the end of the line should also be stripped out.
Example:
Given an input string of:
apples, pears # and bananas
grapes
bananas !apples
The output expected would be:
apples, pears
grapes
bananas
result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
Test.assert_equals(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]), "apples, pears\ngrapes\nbananas")
Test.assert_equals(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")
完成解决方案，以便剥离所有传入的注释标记集之后的所有文本。
该行末尾的所有空格也应被删除。
'''
def solution(a,b):
    pass

'''
In this kata, your task is to create a regular expression capable of evaluating binary strings (strings with only 1s and 0s) and determining whether the given string represents a number divisible by 3.
Take into account that:
An empty string might be evaluated to true (it's not going to be tested, so you don't need to worry about it - unless you want)
The input should consist only of binary digits - no spaces, other digits, alphanumeric characters, etc.
There might be leading 0s.
Examples (Javascript)
multipleof3Regex.test('000') should be true
multipleof3Regex.test('001') should be false
multipleof3Regex.test('011') should be true
multipleof3Regex.test('110') should be true
multipleof3Regex.test(' abc ') should be false
You can check more in the example test cases
Note
There's a way to develop an automata (FSM) that evaluates if strings representing numbers in a given base are divisible by a given number. You might want to check an example of an automata for doing this same particular task here.
If you want to understand better the inner principles behind it, you might want to study how to get the modulo of an arbitrarily large number taking one digit at a time.
在此kata中，您的任务是创建一个正则表达式，该正则表达式能够计算二进制字符串（只有1和0的字符串），并确定给定的字符串是否表示可被3整除的数字。
考虑到：
一个空字符串可能被评估为true（不会被测试，因此您不必担心它-除非您愿意）
输入内容只能包含二进制数字-不能包含空格，其他数字，字母数字字符等。
可能有前导0。
示例（JavaScript）
multipleof3Regex.test（'000'）应该为true
multipleof3Regex.test（'001'）应该为false
multipleof3Regex.test（'011'）应该为true
multipleof3Regex.test（'110'）应该为true
multipleof3Regex.test（'abc'）应该为false
您可以在示例测试用例中查看更多信息
注意
有一种方法可以开发一种自动机（FSM），用于评估表示给定基数中的数字的字符串是否可被给定数字整除。您可能要在此处检查自动机的示例以执行此特定任务。
如果您想更好地理解其背后的内在原理，则可能需要研究如何获取每次取一位数字的任意大数的模。
'''

# compile 函数根据一个模式字符串和可选的标志参数生成一个正则表达式对象。该对象拥有一系列方法用于正则表达式匹配和替换。
# a| b	匹配a或b
# re*	匹配0个或多个的表达式。
# ^ 匹配字符串的开头
# $ 匹配字符串的结尾
# (re)	对正则表达式分组并记住匹配的文本
import re
PATTERN = re.compile(r'^(0|1(01*0)*1)*$')
'''
You might know some pretty large perfect squares. But what about the NEXT one?
Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. 
Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is positive.
Examples:
findNextSquare(121) --> returns 144
findNextSquare(625) --> returns 676
findNextSquare(114) --> returns -1 since 114 is not a perfect
您可能知道一些非常大的完美正方形。 但是下一个呢？
完成findNextSquare方法，该方法查找作为参数传递的整数后的下一个整数理想正方形。 回想一下，整数完美平方是整数n，因此sqrt（n）也是整数。
如果参数本身不是理想的正方形，则应返回-1。 您可以假设参数为正。
例子：
findNextSquare（121）->返回144
findNextSquare（625）->返回676
findNextSquare（114）->因为-1不完美，所以返回-1
'''

import math
def find_next_square(sq):
    sqrt1 = int(math.sqrt(sq))
    # print(sqrt1)
    if math.pow(sqrt1,2) != sq:
        return -1
    else:
        return(int(math.pow(sqrt1+1,2))) 
print(find_next_square(114))


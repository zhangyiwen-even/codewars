'''
Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks whether the two arrays have the "same" elements, with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

Examples
Valid arrays
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write b's elements in terms of squares:
a = [121, 144, 19, 161, 19, 144, 19, 11] 
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
Invalid arrays
If we change the first number to something else, comp may not return true anymore:
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 132 is not the square of any number of a.
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 36100 is not the square of any number of a.
Remarks
a or b might be [] (all languages except R, Shell).
a or b might be nil or null or None or nothing (except in Haskell, Elixir, C++, Rust, R, Shell, PureScript).
If a or b are nil (or null or None), the problem doesn't make sense so return false.
Note for C
The two arrays have the same size (> 0) given as parameter in function comp.
给定两个数组a和b，编写一个函数comp（a，b）（在Clojure中为compSame（a，b）），该函数检查两个数组是否具有“相同”元素，并且具有相同的多重性。 “相同”在这里表示b中的元素是平方的元素，与顺序无关。
例子
有效数组
a = [121，144，19，161，19，144，19，11]
b = [121，14641，20736，361，25921，361，20736，361]
comp（a，b）返回true，因为在b中121是11的平方，14641是121的平方，20736是144的平方，361是19的平方，25921是161的平方，依此类推。如果我们用平方写b的元素，这将变得显而易见：
a = [121，144，19，161，19，144，19，11]
b = [11 * 11、121 * 121、144 * 144、19 * 19、161 * 161、19 * 19、144 * 144、19 * 19]
无效的数组
如果我们将第一个数字更改为其他数字，则comp可能不再返回true：
a = [121，144，19，161，19，144，19，11]
b = [132，14641，20736，361，25921，361，20736，361]
comp（a，b）返回false，因为在b 132中不是任何数量a的平方。
a = [121，144，19，161，19，144，19，11]
b = [121，14641，20736，36100，25921，361，20736，361]
comp（a，b）返回false，因为b中的36100不是a的任何数量的平方。
备注
a或b可能是[]（R，Shell以外的所有语言）。
a或b可能为nil或null或无或无（Haskell，Elixir，C ++，Rust，R，Shell，PureScript中除外）。
如果a或b为nil（或null或None），则该问题没有意义，因此返回false。
C的注意事项
这两个数组具有相同的大小（> 0），这些大小在函数comp中作为参数给出。
'''
# 自己的
# def comp(array1, array2):
#     # alist = []
#     # for i in array1:
#         # alist.append(i**2)
#     alist = [i ** 2 for i in array1]
#     if array2 == [] or alist == []:
#         return False
#     elif len(alist) != len(array2):
#         return False
#     elif sorted(alist) == sorted(array2):
#         return True
#     else:
#         return False
# print(comp([],[121, 14641, 20736, 361, 25921, 361, 20736, 361]))

# 高赞
def comp(array1, array2):
    try:
        return sorted([ i ** 2 for i in array1]) == sorted(array2)
    except:
        return False
print(comp([121, 144, 19, 161, 19, 144, 19, 11],[121, 14641, 20736, 361, 25921, 361, 20736, 361]))
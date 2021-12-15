'''
输入a，b，c，判断三边是否可以构成三角形
Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).

More info:
'''
def is_triangle(a, b, c):
    if a <= 0 or b <=0 or c <=0:
        print("False,didn't work when sides were",a,b,c)
    else:
        if ((a+b > c) and (a-b < c)) and ((a+c > b) and (a-c < b)) and ((b+c > a) and (b-c < a)):
            print("True,didn't work when sides were",a,b,c)
        else:
            print("False,didn't work when sides were",a,b,c)
is_triangle(5,1,2)

# def is_triangl(a, b, c):
#     return (a+b)  > c and (b+c) > a and (a+c) > b
# is_triangl(2,2,2)
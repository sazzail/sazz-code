import math
a = float(input("input the value of a: "))
b = float(input("input the value of b: "))
c = float(input("input the value of c: "))

if ((a + b)>c and (a + c) >b and (c + b)>a):
    s = (a +b +c)/2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("The area of triangle is: ", area)
else:
    print("Triangle Can not be made.")

import math


hight = float(input("Enter isosceles tringle's lenght: "))
base = float(input("Enter isosceles tringle's Base: "))

Area  = (base * math.sqrt((4 * hight * hight) - (base * base)))/4
print("The Area of the Isosceles Triangle: ", Area)
2
import math as m
import cmath as cm
a,b,c=input("Enter a,b,c").split(",")
a=int(a)
b=int(b)
c=int(c)
d=(b**2)-(4*a*c)
if d==0:
    print("Roots are equal and real.\n")
    r=((-b)+m.sqrt(d))/(2*a)
    print("Roots are", r,r)
elif d>0:
    print("Roots are unequal and real.\n")
    r1 = ((-b) + m.sqrt(d)) / (2 * a)
    r2= ((-b) - m.sqrt(d)) / (2 * a)
    print("Root1: ", r1,"Root2", r2)
# else:
#     print("Roots are unequal and complex.\n")
#     r1 = ((-b) + cm.sqrt(d)) / (2 * a)
#     r2= ((-b) - cm.sqrt(d)) / (2 * a)
#     print("Root1: ", r1,"Root2", r2)
else:
    print("Roots are unequal and complex.\n")
    real = (-b)/ (2 * a)
    img =  m.sqrt(-d)/ (2 * a)
    print(f'Roots 1 {real}+i{img}\nRoots 2 {real}-i{img}')
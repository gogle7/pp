import math as m
a=int(input("Enter 1st side\n"))
b=int(input("Enter 2nd side\n"))
c=int(input("Enter 3rd side\n"))
s=(a+b+c)/2
#print(s);
area=m.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area is "+str(area))
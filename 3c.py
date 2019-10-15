a=10
b=20
print ("Swap using temp")
print("Before swap a=",a,"b=",b)
temp=a
a=b
b=temp
print("After swap a=",a,"b=",b)
c=40
d=50
print ("Swap without temp")
print("Before swap c=",c,"d=",d)
c=c+d
d=c-d
c=c-d
print("After swap c=",c,"d=",d)
x=1
y=2
print ("Swap using XOR")
print("Before swap x=",x,"y=",y)
x=x^y
y=x^y
x=x^y
print("After swap x=",x,"y=",y)

s=0
n=int(input("Enter number"))
for i in range(1,n):
    if(n%i==0):
        s+=i
if(s==n):
    print("Perfect Number")
else:
    print("Not Perfect Number")
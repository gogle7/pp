fibo,i,flag=[0,1],0,0
n=int(input("Enter number"))
while(fibo[i]<=n):
    if(n in fibo):
        flag=1
    fibo.append(fibo[i]+fibo[i+1])
    i+=1
if flag:
    print("Number is present in fibonacci series.")
else:
    print("Number is not present in fibonacci series.")

i,flag=1,0
while(i**2<=n):
    if(i**2==n):
        flag=1
        print("Perfect Square")
    i+=1
if(flag==0):
    print("Not perfect square")

i,flag=0,0
while (2**i<=n):
    if (2**i==n):
        flag=1
        print("Perfect power of 2")
    i+=1
if (flag==0):
    print("Not Perfect power of 2")

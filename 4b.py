n=int(input('Enter  number'))
s=0
p=1
for i in range(1,n+1):
    s+=i
    if(i==n):
        print(i,end=" = ")
        print(s)
    else:
        print(i,end=" + ")
for i in range(1,n+1):
    p*=i
    if(i==n):
        print(i,end=" = ")
        print(p)
    else:
        print(i,end=" * ")

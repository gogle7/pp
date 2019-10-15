n=int(input("Enter a number"))
l,count=[],0
for i in range(1,n+1):
    if(n%i==0):
        count+=1
        l.append(i)
if(count<=2):
    print(f"{n} is prime number. The factors are {l}")
else:
    print(f"{n} is composite number. The factors are {l}")
#print(f"{count}")
2
# n=int(input('Enter the number of pebbles'))
# if n%2==0:
#     print("Even")
# else:
#     print("Odd")
n=int(input("Enter the number of bottle"))
l=[]
print("Enter the pebbles in each")
for i in range(n):
    a=int(input())
    l.append(a)
counte,counto=0,0
for i in l:
    if(i%2):
        counto+=1
    else:
        counte+=1
print("Total Odd",counto)
print("Total Even",counte)
l=[]
n=int(input("Enter the number of strings: "))
for i in range(n):
    l.append(input("Enter string: "))
count=0
for i in l:
    if(len(i)>=2 and i[0]==i[-1]):
        count+=1
print("Number of required string: ",count)

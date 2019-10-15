num_list=[]
n=int(input("Enter number of values for num_list: "))
print("Enter the elements:")
for i in range(n):
    num_list.append(int(input()))
mode={}
for i in num_list:
    mode.setdefault(i,0)
    mode[i]+=1
print(mode)
m=0
for i in mode:
    if m <= mode[i]:
        m = mode[i]
print("mode =",m)

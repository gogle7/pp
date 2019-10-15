s1,s2=set(),set()
n1=int(input("Enter the number of elements for set 1: "))
print("Enter the elements: ")
for i in range (n1):
    s1.add(int(input()))
n2=int(input("Enter the number of elements for set 2: "))
print("Enter the elements: ")
for i in range (n2):
    s2.add(int(input()))
s1=list(s1); s2=list(s2)
n1=len(s1);n2=len(s2)
cp=set()
for i in range(n1):
    for j in range(n2):
        cp.add(tuple((s1[i],s2[j])))
cp=sorted(list(cp))
print("The cartesian product is:",cp,sep="\n")

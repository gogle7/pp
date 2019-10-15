countA,countNUM,countS,count=0,0,0,0
s=input("Enter a string: ")
for i in range(len(s)):
    if(s[i].isalpha()):
        countA+=1
    elif(s[i].isdigit()):
        countNUM+=1
    elif (s[i]!=" "):
        countS+=1
    count+=1
print("Number of:\n1.Characters:",count,"\n2.Alphabets:",countA)
print("3.Numbers:",countNUM,"\n4.Special characters(excluding space):",countS)

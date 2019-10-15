A={}
SRN,P_marks,C_marks,M_marks,B_marks=[],[],[],[],[]
n=int(input("Enter the number of records: "))
for i in range(n):
    SRN.append(input("Enter the SRN: "))
for i in range(n):
    P_marks.append(int(input("Enter P marks: ")))
for i in range(n):
    C_marks.append(int(input("Enter C marks: ")))
for i in range(n):    
    M_marks.append(int(input("Enter M marks: ")))
for i in range(n):    
    B_marks.append(int(input("Enter B marks: ")))
for i in range(n):	
    A[SRN[i]]=[P_marks[i],C_marks[i],M_marks[i],B_marks[i]]
##################### PART A ################################################
for i in A:
    print(i,"==>",end=" ")
    for j in A[i]:
        print(j,end=" ")
print()
###################### PART B ###############################################
Total={}
for i in A:
    Total[i]=sum(A[i])
for i,j in sorted(Total.items(), key=lambda a: a[1]):
    print(i,"==>",j)
###################### PART C ###############################################
student_details={}
for i in M_marks:
    student_details[i]=[]
    for j in A:
        if(i==A[j][2]):
            student_details[i].append(j)
print(student_details)

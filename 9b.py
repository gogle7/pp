print("-----------------------UNION-------------------------------")
with open('Q2_file1.txt') as f1,open('Q2_file2.txt') as f2:
    for i,j in zip(f1,f2):
        if set(i.split()) == set (j.split()):
            print(i.strip())        
        else:
            print(i.strip(),j.strip())
            
print("---------------------INTERSECTION--------------------------")
with open('Q2_file1.txt') as f1,open('Q2_file2.txt') as f2:
    for i,j in zip(f1,f2):
        if set(i.split()) == set (j.split()):
            print(i.strip())

print("--------------------(set1 - set2)--------------------------")
with open('Q2_file1.txt') as f1,open('Q2_file2.txt') as f2:
    for i,j in zip(f1,f2):
        if set(i.split()) == set (j.split()):
            pass
        else:
            print(i.strip())
            
print("---------------------SYMMETRIC DIFFERENCE-------------------")
with open('Q2_file1.txt') as f1,open('Q2_file2.txt') as f2:
    for i,j in zip(f1,f2):
        if set(i.split()) == set (j.split()):
            pass
        else:
            print(i.strip(),j.strip())

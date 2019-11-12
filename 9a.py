f=open("Q1_Test.txt",'r')
f1=open("Q1_Output.txt",'w')

for i,j in enumerate(f.readlines(),1):
        f1.write(str(i)+" "+j)

f1.close()
f.close()

out=open('Leaders.txt','w')
out.writelines("Leaders are:\nLine No.\tCode Snippet\n")

with open("Input File.py",'r') as IP:
    for j,i in enumerate(IP,1):
        if i.strip().endswith(":"):
            out.writelines(str(j)+'\t'+i.strip()[:-1]+'\n')
            
out.close()

out=open("Functions.txt",'w')
out.writelines("Functions are:\nLine No.\tLine of code\n")

with open("Input File.py",'r') as IP:
    for i,j in enumerate(IP,1):
        if j.strip().startswith("def"):
            out.writelines(str(i)+"\t"+j.strip()[:-1]+"\n")    

out.close()

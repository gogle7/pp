class Matrix:
    def __init__(self,l,b):
        self.mat=[[0 for i in range(b)] for j in range(l)]
        self.length=l
        self.breadth=b
        
    def read(self,name):
        print("\n"+name)
        for i in self.mat:
            for j in i:
                print(j,end=" ")
            print()
        print()
        
    def populate(self,name):
        print("Enter the elements in matrix: ")
        for i in range(len(self.mat)):
            for j in range(len(self.mat[i])):
                self.mat[i][j]=int(input())
        self.read(name)
        
    def add(self,matA,name):
        if((self.length!=matA.length) and (self.breadth!= matA.breadth)):
            print("Error: Unequal matrix")			
            return
        for i in range(len(self.mat)):
            for j in range(len(self.mat[i])):
                self.mat[i][j]+=matA.mat[i][j]
        self.read(name)

l,b=input("Enter Length and breadth of matrix:").split(",")
l=int(l)
b=int(b)
MatA=Matrix(l,b)
MatA.populate("Matrix A:")
l,b=input("Enter Length and breadth of matrix:").split(",")
l=int(l)
b=int(b)
MatB=Matrix(l,b)
MatB.populate("Matrix B:")
MatA.add(MatB,"Matrix A:")	

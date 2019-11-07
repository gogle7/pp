def is_square(n):
    if int(n**0.5)==n**0.5:
        return True
    else:
        return False
def is_even(n):
    if n%2:
        return False
    else:
        return True
n=int(input("Enter the upper limit"))
for i in range(2,n+1,2):
    if is_even(i) and is_square(i):
        print(i,end=" ")
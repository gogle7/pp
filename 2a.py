n = input("Enter a string of 4 length")
a=""
for i in n:
    #print(f"The ASCII value of '{i}' is {ord(i)}")
    a+=str(ord(i))
print(f"The encoded value is {a}")


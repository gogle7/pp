def Highest(marks, name):
    if len(marks) != len(name):
        return "Record Mismatch"
    max_marks = max(marks)
    index = []
    for i in range(len(marks)):
        if marks[i] == max_marks:
            index.append(i)
    res = []
    for i in index:
        res.append(marks[i])
        res.append(name[i])
    return res


def enter(l, n, text=False):
    print("Enter the elements")
    for i in range(n):
        if (text):
            l.append(input())
        else:
            l.append(int(input()))


marks, names = [], []
n1 = int(input("Enter the no of result"))
enter(marks, n1)
n2 = int(input("Enter the no of names"))
enter(names, n2, True)
print(marks, names, sep="\n")
print(Highest(marks, names))

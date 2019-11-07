def mod(d):
    res={}
    for i in d:
        if d[i] not in res:
            res[d[i]]=[]
            res[d[i]].append(i)
        else:
            res[d[i]].append(i)
    return res
x={'apple':'fruit','cat':'mammal','mango':'fruit','dog':'mammal','veg':'beans'}
print(mod(x))
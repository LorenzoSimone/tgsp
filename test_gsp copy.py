def deleteIndexes(l,l2, fun):
    for i in list(range(len(l)))[::-1]:
        if(fun(l[i])):
            del l[i]
            del l2[i]
    return l,l2

a = [3,20,4,5,30,40,6,7]
print(a)
a = deleteIndexes(a,list(set(a)), lambda d: d>10)
print(a)
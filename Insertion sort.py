cisla=[1,3,6,4,5,2,8,9,7]

def insertion_sort(val):
    pos=0
    for i in range(len(val)-1):
        minimum=None
        for j in range(i,len(val)):
            if minimum is None or minimum>val[j]:
                pos,minimum=val[i],val[j]
                val[j],val[i]=pos,minimum
    return val
print(insertion_sort(cisla))

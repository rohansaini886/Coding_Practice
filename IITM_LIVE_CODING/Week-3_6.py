def quicksort(L,l,r):
    if (r-l) <= 1:
        return L
    (pivot,lower,upper) = (L[l][1],l+1,l+1)
    for i in range(l+1,r):
        if L[i][1]>pivot:
            upper=upper+1
        else:
            L[i],L[lower]=L[lower],L[i]
            (lower,upper)=(lower+1,upper+1)
    L[l],L[lower-1]=L[lower-1],L[l]
    lower=lower-1
    quicksort(L,l,lower)
    quicksort(L,lower+1,upper)
def Arrange(l):
    count = 0
    for i in range(len(l)):
        if l[i][2] == "F":
            l[i], l[count] = l[count], l[i]
            count += 1
    for i in range(count):
        for j in range(count - 1):
            if l[j][1] > l[j + 1][1]:
                l[j + 1], l[j] = l[j], l[j + 1]
                
    for i in range(len(l) - count):
        for j in range(count, len(l) - 1):
            if l[j][1] > l[j + 1][1]:
                l[j + 1], l[j] = l[j], l[j + 1]

L = eval(input())
Arrange(L)
print(L)

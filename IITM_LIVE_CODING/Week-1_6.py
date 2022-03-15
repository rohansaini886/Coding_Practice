def histogram(l):
    w = []
    x = []
    y = []
    z = []
    for i in l:
        if i in y:
            continue
        else:
            w.append(l.count(i))
            y.append(i)
            x.append((i, l.count(i)))
    ans = []
    for i in set(w):
        temp = []
        for j in range(len(x)):
            if x[j][1] == i:
                temp.append(x[j])
        for j in range(len(sorted(temp))):
            ans.append(sorted(temp)[j])
    return ans


L=eval(input())
print(histogram(L))

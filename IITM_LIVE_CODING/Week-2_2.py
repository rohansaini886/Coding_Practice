def sortTuples(l):
    x = []
    ans = []
    for i in range(len(l)):
        x.append(l[i][1])
    x = sorted(x)
    for i in range(len(x)):
        for j in range(len(x)):
            if l[j][1] == x[i]:
                ans.append(l[j])
    for i in range(len(ans)):
        print(*ans[i])

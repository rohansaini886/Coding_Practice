n, d = map(int, input().split(" "))
l = list(map(int, input().split(" ")))
count = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        else:
            if 0 <= l[i] - l[j] <= d:
                # print(l[i], l[j])
                if l[i] == l[j]:
                    count += 1
                else:
                    count += 2
print(count)

n = int(input())
count = 2
for i in range(2, n + 1):
    if count % n == 0:
        print(n, end = ' ')
    else:
        print(int(count % n), end = " ")
    count += i

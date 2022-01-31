x, y = map(int, input().split(" "))
maxi = max(x, y)
l = [1, 2, 3, 4, 5, 6]
count = 6 - l.index(maxi)
# print(count)
if count == 1:
    print('1/6')
elif count == 2:
    print('1/3')
elif count == 3:
    print('1/2')
elif count == 4:
    print('2/3')
elif count == 5:
    print('5/6')
elif count == 6:
    print('1/1')
else:
    print('0/1')

for _ in range(int(input())):
    tr = int(input())
    ram_task = list(map(int, input().split(' ')))
    dr = int(input())
    ram_dare = list(map(int, input().split(' ')))
    ts = int(input())
    sham_task = list(map(int, input().split(' ')))
    ds = int(input())
    sham_dare = list(map(int, input().split(' ')))
    lose = False
    for i in sham_task:
        if i not in ram_task:
            lose = True
    for i in sham_dare:
        if i not in ram_dare:
            lose = True
    if lose:
        print('no')
    else:
        print('yes')

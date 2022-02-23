for _ in range(int(input())):
    x1,y1=map(int,input().split())
    x2,y2=map(int,input().split())
    x3,y3=map(int,input().split())
    if(y1==y2>y3):
        print(abs(x2-x1))
    elif(y1==y3>y2):
        print(abs(x3-x1))
    elif(y3==y2>y1):
        print(abs(x2-x3))
    else:
        print(0)

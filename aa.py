h,w = map(int,input().split())
pan = [[0 for _ in range(w)] for _ in range(h)]
n = int(input())
for i in range(n):
    l,d,x,y = map(int,input().split())
    if d == 0:
        for j in range(l):
            pan[x-1][y-1] = 1
            y+=1
    elif d == 1:
        for k in range(l):
            pan[x-1][y-1] = 1
            x+=1
for i in range(h):
    for j in range(w):
        print(pan[i][j],end=" ")
    print("\n")
loc = [[0 for _ in range(19)] for _ in range(19)]
for i in range(19):
    loc[i] = list(map(int,input().split()))

n = int(input())

for i in range(n):
    x,y = map(int,input().split())
    for j in range(19):
        for k in range(19):
            if loc[x][k] == 0:
                loc[j][k] == 1
            else:
                loc[j][k] == 0
2 2
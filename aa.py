h, w = map(int, input().split())
s = [[0 for i in range(h)] for j in range(w)]

n = int(input())
for i in range(n):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for i in range(l):
            s[x-1][y-1] = 1
            y+=1
    elif d == 1:
        for i in range(l):
            s[x-1][y-1] = 1
            x +=1

for i in range(len(s)):
    for j in range(len(s[i])):
        print(s[i][j], end=" ")
    print()


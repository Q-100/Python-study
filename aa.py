s = []
for i in range(10):
    s.append(list(map(int, input().split())))
x,y = 1,1
check = 0
if s[x][y] == 2:
    check = 1
s[x][y] = 9

while check == 0:
    if s[x][y + 1] == 0:
        y += 1
        s[x][y] = 9

    elif s[x][y + 1] == 1:
        if s[x + 1][y] == 0:
            x += 1
            s[x][y] = 9
        elif s[x + 1][y] == 1:
            s[x][y] = 9
            break
        else:
            s[x + 1][y] = 9
            break
    else:
        s[x][y + 1] = 9
        break

for i in range(len(s)):
    for j in range(len(s[i])):
        print(s[i][j],end =" ")
    print(" ")
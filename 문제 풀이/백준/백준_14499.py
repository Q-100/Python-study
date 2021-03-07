dice = [0, 0, 0, 0, 0, 0]
loc = []
N, M, x, y, K = map(int, input().split())
for _ in range(N):
    a = [int(z) for z in input().split()]
    loc.append(a)
command = map(int, input().split())
for dir in command:
    if dir == 1:
        if y + 1 == M:
            continue
        y += 1
        tmp = dice[0]
        dice[0] = dice[2]
        dice[2] = dice[5]
        dice[5] = dice[3]
        dice[3] = tmp
    elif dir == 2:
        if y - 1 < 0:
            continue
        y -= 1
        tmp = dice[0]
        dice[0] = dice[3]
        dice[3] = dice[5]
        dice[5] = dice[2]
        dice[2] = tmp
    elif dir == 3:
        if x - 1 < 0:
            continue
        x -= 1
        tmp = dice[0]
        dice[0] = dice[4]
        dice[4] = dice[5]
        dice[5] = dice[1]
        dice[1] = tmp
    elif dir == 4:
        if x + 1 == N:
            continue
        x += 1
        tmp = dice[0]
        dice[0] = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[4]
        dice[4] = tmp
    if loc[x][y] == 0:
        loc[x][y] = dice[5]
    else:
        dice[5] = loc[x][y]
        loc[x][y] = 0
    print(dice[0])

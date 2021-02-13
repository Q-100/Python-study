n = int(input())
a = map(int,input().split())
s = [0 for i in range(23)]
for i in a:
    s[i-1] += 1

print(s)
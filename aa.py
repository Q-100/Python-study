a = map(int, input().split())
def check(a):
    for c in a:
        if c == 0:
            return
        else:
            print(c)

check(a)

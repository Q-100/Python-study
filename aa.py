s = str(input())
s_len = len(s)

for i in s:
    s_len = s_len-1
    for j in range(s_len):
        i = int(i)*10
    print("[{i}]".format(i=i))

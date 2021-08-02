s = "A man, a plan, a canal: Panama"

tmp = []
for i in s:
    if i.isalnum():
        tmp.append(i.lower())
tmp = "".join(tmp)
a = reversed(tmp)
print(tmp)
print(a)
print(tmp == reversed(tmp))
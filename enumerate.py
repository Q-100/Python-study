# a = ["a1","b2","c3"] 를 인덱스와 함께 뽑아내는 방법들
a = ["a1", "b2", "c3"]
for i in range(len(a)):
    print(i, a[i])

i = 0
for z in a:
    print(i, z)
    i += 1

for i, v in enumerate(a): # enumerate는 인덱스와 값을 같이 출력해줌
    print(i, v)

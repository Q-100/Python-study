t = (1, "korea", 3.5, 1)
t = t + (3, 5)  # 이런식으로 더할수도 있음
print(t)

h = (350)  # 튜플은 한개만 존재할 수 없음(이건 그냥 정수임)
print(type(h))
h = (350,)  # 이런식으로하면 튜플로 만들 수 있음
print(type(h))
h = 1, 2, 3, 4, 5  # 이런식으로 해도 튜플임(괄호가 필수가 아님)
print(type(h))


def minmax(items):
    return min(items), max(items)


min1, max1 = minmax([1,2,3,4,5])
print(type(min1),min1,max1)
print(type(minmax([1,2,3,4,5])),minmax([1,2,3,4,5])) # 튜플로 반환함

a = [[1,2,3],[4,5,6]]
b=a
b[0] = 3
print(b)

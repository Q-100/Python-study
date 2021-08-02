# 딕셔너리의 키는 무조건 immutable한 객체여야됨
import collections

a = {1: 5, 3: 5}

a = {"a": 5, "a": 3}  # 값은 중복될 수 있지만 키값은 중복되면 맨 마지막 키값만 적용되고 없어짐
print(a)

d = {'abc': 1, 'def': 2}
print(d["abc"])  # 딕셔너리는 순서가 없어서 인덱스로 접근 불가능 -> 대신 키값으로 접근해야됨

d["abc"] = 3  # 딕셔너리는 mutable한 객체이기 때문에 수정이 가능(키로 접근하여 수정)
print(d)
d["aaa"] = 5  # 이런식으로하면 새로운 키와 값을 만들 수 있음
print(d)

d = dict(alice=5, asd=3)  # 이런식으로 선언 할 수 도 있음

k = [["alice", 5], ["bob", 3]]  # 이런 리스트를
a = dict(k)  # 이런식으로 변환 가능(튜플안 리스트, 리스트안 튜플, 튜플안 튜플 등 키와 값을 나란히 입력하면 딕셔너리로 변환 가능)
print(a)

# 딕셔너리도 copy를 사용하면 얕은 복사가 됨, b= dict(a)를 사용하면 객체가 다르게 복사되지만 내용물이 mutable한 객체 일시 똑같은 얕은복사됨

a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
a.update({"alice": 5, "bob": 99})  # 여러개를 수정할려면 update를 사용해야함
print(a)

for key in a:  # 딕셔너리를 for문을 돌리면 key값이 할당됨(순서는 임의적임, 순서보장되지않음)
    print(key)

for value in a.values():  # value값을 얻을려면 values()를 사용해야함
    print(value)

for key, value in a.items():  # key와 value값을 같이 출력할려면 items를 사용
    print(key, value)

print("alice" in a)  # 딕셔너리에서 in은 key값에 한해서 사용가능

del a["alice"]  # del로 삭제가능
print(a)

print([k for k, v in a.items() if v == 99])  # 이런식으로 key값을 찾던가

aa = {'0': 'AA', '1': 'BB', '2': 'CC'}  # 자주 value값을 찾아야된다면 키와 값을 뒤집어서 저장함(대신 값이 중복될수도있다는 단점)
bb = {v: k for k, v in aa.items()}  # {'AA': '0', 'BB': '1', 'CC': '2'}
print(bb["AA"])

a = {}
a["A"] = 1
a["b"] = 2
print(a)

a = [1, 2, 3, 4, 5, 5, 5, 6, 6]
b = collections.Counter(a)
print(b[5] # 5의 갯수 출력
print(b.most_common(2)) # 가장 많은 갯수를 가진 요소 2개 출력

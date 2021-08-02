s = {"a", 3, (1, 2, 3)}  # set(집합)은 딕셔너리와 다르게 key가 없음(mutable한 객체 사용불가능)
print(s)

s = set()  # 집합은 딕셔너리와 똑같은 중괄호를 사용하기 때문에 s = {}로 선언 불가능(set()로 선언)

s = {1, 2, 3, 1, 1, 5}  # 중복된 값은 자동으로 삭제되서 저장됨
print(s)

for i in s:  # 집합은 순서가 없음(랜덤으로 나옴)
    print(s)

s.add(50)  # 집합에 추가는 add()를 사용
print(s)

s.update([1, 3, 5, 9])  # 여러개를 추가 할 때는 update()를 사용(update는 iterable한 객체만 인자로 가능)
print(s)

s.remove(5)  # 삭제 시 존재하지 않으면 에러발생
s.discard(5)  # 삭제 시 존재하지 않아도 에러발생 하지 않음

b = set(s)  # 얕은 복사에 해당
b = s.copy()  # 얕은 복사에 해당

c = s | b # 합집합(== a.union(b))
c = s & b # 교집합(== a.intersection(b))
c = s - b # 차집합(== a.difference(b))
c = s ^ b # 대칭 차집합(== a.symmetric_difference(b))

c &= b # 이런식으로 하면 c = c & b와 같음(c의 id도 안바뀌고 그대로임)

# a.issubset(b) -> 부분 집합 여부 확인
# issuperset(b) -> 부분집합 여부확인의 반대
# isdisjoint(b) 교집합이 있으면 true 없으면 false
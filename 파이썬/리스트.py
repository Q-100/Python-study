import copy

print(["a", 354, True])  # 리스트에는 여러타입이 공존할 수 있음

b = list()
b = [1, 2, 3, 4]
c = []
c = [1, 2, 3, 4]

b.append(1)  # 맨뒤에 삽입
print(b)

print(list("가나다"))  # 문자열을 리스트로 변환

s = "show how to index into sequences"

q = s.split()  # 띄어쓰기를 기준으로 나눠서 리스트로 생성
z = list(s)  # 한글자씩을 기준으로 나눠서 리스트로 생성

print(q)
print(z)

print(q[:3] + q[3:] == q)  # 각각 슬라이싱한 리스트를 합치면 기존의 리스트와 같음

v = q.copy()  # 이런식으로 하던가 아니면 v = list(q)
u = q  # 이런식으로 하면 q의 메모리 주소값을 저장하게됨 -> u를 수정하면  q도 수정됨
print(u)
print(v)

print(v[::2])  # 처음부터 2칸씩 띄어서 출력
print(v[::-1])  # 거꾸로 출력

##### mutable과 imutable #####

a = [1, 2, 3]  # mutable한 객체는 수정을 하게되도 메모리주소값이 안바뀜
b = a
b[0] = 5
print(b, a)  # 리스트는 mutable한 객체임(변하기쉬운) -> 메모리주소값을 b에 저장했기 때문에 같이수정됨

a = "abcd"  # 똑같이 b를 a에 할당하면 같은 메모리 주소를 바라보게 됩니다.
b = a
b = "abc"  # 하지만 b에 다른 값을 할당하면 재할당이 이루어지며 메모리 주소가 변경됩니다.
print(a, b)  # 고로 a와 b는 다른 값을 가집니다.

# 리스트를 슬라이싱 하여 b에 대입하면 id값이 바뀜 -> 대신 리스트안의 mutable한 객체가 존재할경우 그 값은 기존의 a리스트 안의 객체와 같은 id를 가지는 문제가있음
# copy메소드도 얕은 복사임(위와 같은 문제가있음)

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)  # 이런식으로 깊은 복사를 사용하면 내부의 객체까지 모두 새롭게 카피됨(주소값 모두변경)
a[1].append(5)
print(a)
print(b)

a = [[5, 3]]  # 리스트의 반복도 얕은복사의 문제가 있음
b = a * 3
a[0].append(2)  # a를 수정했는데 a를 3번 반복한 b의 모든 객체들에 a의 수정된 값이 저장됨
print(b)

a = ["서울", "인천", "제주도"]
print(a.index("인천"))  # 찾을 문자열 또는 문자를 찾아 인덱스를 반환함(없으면 오류), index("인천",1,3)이런식으로 1~3 인덱스 사이에서 찾을 수도 있음, 첫번째로찾은것만 반환
print(a.count("서울"))  # 매칭 되는 갯수를 반환함
print("서울" in a)  # 있을 시 true 반환

a.insert(1, "대전")  # 1번째 인덱스에 "대전"문자열 추가
print(a)
a.extend(["부산", "독도", "서울"])  # 리스트를 맨뒤에 추가
print(a)

del a[1]  # 1번째 인덱스에 있는 요소 삭제
print(a)
a.remove("서울")  # == del a[a.index("서울")]      // 못찾는다면 에러발생
print(a)

a.reverse()  # 문자열 뒤집기
print(a)

a = [1, 10, 5, 7, 6]
a.sort()  # 인자가 없으면 오름차순으로 정렬
print(a)
a.sort(reverse=True)  # 이런식으로 하면 내림차순
print(a)
# a.sort(key=len) # TODO 이거 다시공부하기

print(sorted(a))  # sorted는 원형을 변형시키지 않고 정렬된 리스트를 반환함

print(reversed(a))  # reversed는 원형을 변형시키지 않고 거꾸로 뒤집어 반환 -> iterable한 객체를 반환하기 때문에 list로 확인해야됨
print(list(reversed(a)))  # 이런식으로 list로 확인

# 리스트 컴프리헨션
a = [i for i in range(10)]
print(a)

a = list(i for i in range(10))
print(a)

a = [i * 2 for i in range(10)]
print(a)

a = [i * 2 for i in range(10) if i % 2 == 0] # 0~9까지 생성을 하는데 그 중 2로나눈 나머지가 0인 수를 2를 곱해서 리스트에 저장
print(a)

a = [i*j for i in range(2,10) for j in range(1,10)] # 이런건 뒤에서 부터 시작함(뒤에꺼 다돌고 앞에꺼하나늘고 이런식)
print(a)
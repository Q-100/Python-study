# 람다식은 함수의 인수부분을 간단하게 하기위해서 사용, 괄호밖의 변수도 사용가능

def plus_ten(x):
    return x + 10


print(plus_ten(10))

lambda x: x + 10  # 람다는 익명함수라고도 불리는데 이름이 없기때문에 호출이 불가능하다
# lambda 매개변수: 반환값으로 사용할 식

ten = lambda x: x + 10  # 이런식으로 변수에다가 저장해서 사용함
print(ten(10))

print((lambda x: x + 10)(10))  # 이런식으로 괄호로 묶으면 변수에 저장하지않고 바로 호출가능

y = 10
print((lambda x: x + y)(5))  # 밖에있는 변수들을 사용할수있단점이 일반함수와 다름

print(list(map(plus_ten, [1, 2, 3])))  # map은 원래 map(int,[1,2,3])이런식으로 사용해왔지만 함수를 사용할수도있음

print(list(map(lambda x: x + 10, [1, 2, 3])))  # [1,2,3]이 차례대로 람다식에 들어가서 반환됨

print((lambda: 3)())  # 매개변수가 없는 식(바로 3출력)
print((lambda: y)())  # 매개변수가 없는 식 (바로 y출력,y는 밖에서 선언된 변수)

# 람다 조건식
print(list(map(lambda x: str(x) if x % 3 == 0 else x, [1, 2, 3, 4, 5, 6, 7])))  # 3의 배수만 문자변환 나머진 그냥출력
print(list(map(lambda x: str(x) if x % 2 == 0 else float(x) if x % 3 == 0 else x, [1, 2, 3, 4, 5, 6])))
# 2의 배수일경우 문자변환 아닐시 다음단계로 이동 3의 배수일시 실수변환 나머지는 그냥출력(이런경우는 그냥 함수만들어서 쓰는게나음)

# map에 객체 여러개 넣기
print(list(map(lambda x, y: x + y, [1, 2, 3, 4], [2, 3, 4, 5])))  # 2개 사용
print((lambda x, y: x * y)(5, 6))  # 행렬 곱셈은 안됨(numpy써야할듯)


# filter 사용하기
# filter는 반복 가능한 객체에서 특정 조건에 맞는 요소를 가져오는데 filter에 적용한 함수의 값이 True인 값만 가져옴
# filter(함수,반복가능한객체)

def f(x):
    return 5 < x < 10


print(list(filter(f, [1, 2, 3, 4, 5, 6, 7])))  # filter를 바로 출력해버리면 map처럼 객체주소 반환됨

print(list(filter(lambda x: 5 < x < 10, [1, 2, 3, 4, 5, 6, 7])))  # 람다식으로 간소화

print([i for i in [1, 2, 3, 4, 5, 6, 7] if 5<i<10]) # TODO filter대신에 리스트표현식으로 하는 것이 더 효율적

# reduce 사용하기
# reduce는 반복 가능한 객체의 각 요소를 지정된 함수로 처리한 뒤 이전 결과와 누적해서 반환하는 함수
from functools import reduce  # reduce는 파이썬3부터 내장함수가아님


# reduce(함수,반복가능한객체)

def f(x, y):
    return x + y


print(reduce(f, [1, 2, 3, 4, 5]))  # x=1,y=2 -> x=3, y=3 ...
print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))  # 람다식으로 줄임


x = 0
for i in range([1, 2, 3, 4, 5]):
    x = x+i

print(x)

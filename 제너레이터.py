# 제너레이터는 이터레이터를 생성해주는 함수
# 제너레이터는 만드는 조건만을 가지기 때문에 1억개의 숫자를 생성해도 메모리는 만드는 조건의 크기만큼만 가짐


def number_generator():
    yield 0
    yield 1
    yield 2


for i in number_generator():
    print(i)
g = number_generator()
print(g.__next__())
print(g.__next__())
print(number_generator().__next__())
print(number_generator().__next__())

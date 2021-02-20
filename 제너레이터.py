# 제너레이터는 이터레이터를 생성해주는 함수


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

import sys


def get_natural_number():
    """
    :return: yield n에는 무한대의 숫자를 가진 제너레이터가있음
    """
    n = 0
    while True:
        n += 1
        yield n


z = get_natural_number()  # z에 제너레이터를 저장
for _ in range(5):
    print(next(z))  # next를 이용해서 무한대의 숫자를 가진 제네러이터에서 값을 한개씩 꺼내옴


def generator():
    yield 1
    yield "Test"
    yield True


g = generator()
# for _ in range(len(list(g))): # stopIteration 뜨는 이유 : 제너레이터는 한번 값을 뽑아내면 끝임 len(list(g))에서 한번뽑앗기때문에 더이상 뽑을게없음
#    print(next(g)) # 그리고 for in range()에서 range가 제너레이터임


a = [n for n in range(100)]
b = range(100)
print(len(a) == len(b)) # 둘다 100개의 리스트가 만들어짐
print(sys.getsizeof(a)) # 하지만 a에는 이미 생성된 값이 들어가있고
print(sys.getsizeof(b)) # b에는 생성해야한다는 조건만 들어가있어서 메모리차이가 매우심하다
# 대신 생성 조건만 있다고해서 인덱스 접근이 불가능할 것같지만 인덱스 접근시에 바로 생성되록 구현되어있음

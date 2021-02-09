m = [1, 5, 7]


def test(k):
    k.append(5)  # 이런식으로 함수안에 인자로 넘긴 객체가 mutable한 객체일경우 기존의 객체도 같이 바뀜
    return print("m = ", k)


test(m)
print(m)


def test1(k):
    k = [1, 2, 3, 4, 5]  # 재할당을 해버리면 메모리 주소가 바뀌기 때문에 기존의 객체는 수정되지 않음
    return print("k = ", k)


test1(m)
print(m)  #


def test2(k):
    return k  # 리턴만 하는 경우에도 메모리 주소는 안바뀜


test2(m)
print(m)


def test3(k, j=3):  # 이런식으로 생성자를 대체하게 기본적으로 초기화가능(인자로 갯수에 맞게 안넘겨줘도 기본값이 있으면 ㄱㅊ)
    print(f"k = {k} j = {j}")


test3(1)


# 이런 함수 기본값은 함수가 실행될때마다 초기화가 되는 것이 아닌 함수가 처음 평가될때를 기준으로 함
# 시간함수같은경우를 기본값으로 정의해두면 처음 함수가 실행될때의 값이 저장되어 시간 변동이 없음

def test4(a, b, c):
    return print(a, b, c)


test4(3, 5, 4)  # 기본 인자 전달 방법

test4(a=3, c=4, b=1)  # 키워드 인자 전달 방법

a = [1, 2, 3]
test4(*a)  # 이런식으로 *을 이용하여 리스트나 튜플같이 인덱스가 있는 객체를 위치 인자 언패킹하여 인자 전달 가능
test4(*(1, 2, 3))  # 변수 대신 바로 입력가능


def test5(*k):
    return k[0], k[1], k[2]


# 위치 인자 언패킹을 사용하면 아래와같이 함수 매개변수랑 인자가 맞지 않아도 사용가능
print(test5(*(1, 2, 3, 4)))


def test6(a, *k):  # 고정인자와 같이 사용할 때는 위치인자가 무조건 고정인자 뒤에 있어야됨
    return print(k[0], a, k[1])


test6(6, *(1, 2, 3))  # 고정 인자와 같이 사용도 가능함


def test7(departure, arrival, flighttime):  # 딕셔너리는 **로 사용가능
    print("출발지는", departure)
    print("도착지는", arrival)
    print("비행시간은 ", flighttime)


a = {"departure": "seoul", "arrival": "newyork", "flighttime": 3}
test7(**a)

test7(**{"departure": "seoul", "arrival": "newyork", "flighttime": 3}) # 이런식으로 직접 입력가능

def test8(**k): # 이렇게도 가능(근데 별두개 없애고 쓰는거랑 똑같음 ㅡㅡ)
    print("출발지는", k['departure'])
    print("도착지는", k["arrival"])
    print("비행시간은 ", k['flighttime'])

test8(**a)
k = 1
def terst9():
    k = 5
    print(k)

terst9()
print(k)
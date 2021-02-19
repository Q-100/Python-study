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

test7(**{"departure": "seoul", "arrival": "newyork", "flighttime": 3})  # 이런식으로 직접 입력가능


def test8(**k):  # 이렇게도 가능(근데 별두개 없애고 쓰는거랑 똑같음 ㅡㅡ)
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


def pass_test():
    """
    파이썬은 함수내용을 적지않으면 오류가남 나중에 추가할 거면 pass로 일단 해놔야됨
    """
    pass


print(pass_test.__doc__)  # 독스트링 출력
help(pass_test)  # help에 함수를 넣으면 함수의 이름, 매개변수, 독스트링을 도움말 형태로 출력해줌


def add_sub(a, b):  # 반환 값으로 여러개를 할 수 있음(튜플로 반환)
    return a + b, a - b


x = add_sub(5, 2)  # 한개의 변수에 튜플로 저장됨(갯수에 맞게 하면 각자 언패킹되서 들어감)
print(x)


def print_number(*args):
    """
    매개변수 앞에 *을 붙이면 유동적으로 매개변수를 받을 수 있음
    :param args: 반복이 가능한 형태 갯수 아무거나
    :return: 출력
    """
    for arg in args:
        print(arg)


x = [1]
print_number(x)
y = [1, 2, 3, 4]
print_number(y)


def print_number1(a, *args):
    """
    다음 처럼 꼭 받아야하는 고정인수가 있을 경우 이렇게 받을 수 있음
    대신 가변인수가 고정인수보다 앞에 있으면 안됨
    :param a: 따로 받아야하는 인수
    :param args: 갯수 상관없이 받는 인수
    :return: 출력
    """
    print(a)
    print(args)


print_number1(x)  # 이런식으로 가변인수에는 값이 없어도됨


def personal(name, age, address):
    print('이름:', name)
    print('나이:', age)
    print('주소:', address)


personal(age=30, address="서울", name="김규백")  # 키워드 인수를 이용하여 인자 순서에 맞지않게 넣을 수 있음
# print(10,20,30,sep=":",end=" ") 여기서 sep과 end도 키워드 인수임

x = {'name': "김규백", "age": "30", "address": "서울시"}


def personal1(**kwargs):
    print('이름:', name)
    print('나이:', age)
    print('주소:', address)


personal1(**x)

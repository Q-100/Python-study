class Person:  # self : 인스턴스 자기 자신을 뜻함
    def __init__(self, *args):
        """
        속성을 정의할 때는 __init__을 사용
        :param hello: 이렇게 인자를 받아서 사용도 가능
        :param *args: 키워드 인수 가능
        :param **kwargs: 딕셔너리 언패킹도 가능
        ★ 메서드안에서 속성을 정의 할 경우 외부에서 그 메서드를 호출할때까지 사용불가능
        """
        self.hello = args[0]
        self.check = args[1]

    def walk(self):
        print(self.hello)
        print(self.check)

    def work(self):
        self.walk()  # 클래스 내의 메서드를 사용할려면 self.메서드 로 호출해야함


a = ["ㅋㅋ", "ㅎㅎ"]
james = Person(*a)
# james.hello = "싫음"
james.work()


class Person1:
    __slots__ = ["name", 'age'] # __slots__은 지정한 속성만 만들고 사용가능하게 함


maria = Person1()
maria.name = "이건 가능"
maria.age = "이것도 가능"
# maria.address = "이건 불가능" address는 slots에 정의되어있지 않아 사용불가능

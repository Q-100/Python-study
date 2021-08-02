class Person:
    bag = []  # 클래스 변수(인스턴스 생성하지 않아도 사용가능한 모든 인스턴스들의 공통적인 변수)

    # __bag = [] 이런식으로 클래스 변수도 비공개 변수로 할 수 있음(private)

    def put_bag(self, stuff):
        self.bag.append(stuff)  # 클래스 변수를 사용하는데 부적합함, Person.bag.append 이게 더 명확


john = Person()
john.put_bag("가방")

maria = Person()
maria.put_bag("열쇠")

print(Person.bag)  # 클래스에서 바로 접근 가능


class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def add(a, b):
        """
        @staticmethod를 붙여 정적메소드로 표현
        정적메서드는 인스턴스 속성에 접근이 불가능하고 클래스에서 바로 접근이 가능하다
        인스턴스 속성, 인스턴스 메서드가 필요없을 때 사용
        :param a:
        :param b:
        :return:
        """

        print(a + b)

    def mul(self, a, b):
        print(a * b)


Calc.add(3, 5)  # 클래스에서 바로 접근가능


# class Person1:
#     a = 0
#
#     def __init__(self):
#         self.a = 5
#         # Person1.a = 5
#
#     @classmethod
#     def print(cls):
#         print(cls.a)
#
#
# james = Person1()
# james.print()
# 클래스메서드_심사 보고 이해할것

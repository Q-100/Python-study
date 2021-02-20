class Person:
    def __init__(self):
        self.breath = "숨쉬는중"

    def breath_print(self):
        print(self.breath)

    def greeting(self):
        print("안녕하세요")


class Student(Person):
    def __init__(self):
        self.grade = "A"
        super().__init__()  # super가 없으면 조상클래스의 __init__이 실행되지 않기 때문에 super로 생성자를 초기화해줘야됨
        # 만약 Person을 상속받은 Student클래스에 __init__이 없으면 super를 사용하지않아도 자동으로 조상클래스의 __init__이 실행됨

    def grade_print(self):
        print(self.grade)

    def greeting(self):
        """
        greeting 함수는 조상클래스에도 존재하고 안녕하세요 라는 문자열이 반복되서 비효율적임
        super().greeting을 사용하면 조상클래스의 greeting을 사용할 수 있음 -> 저걸 사용하고 Student클래스에선 감사합니다만 출력하면됨
        :return:
        """
        print("안녕하세요 감사합니다")


james = Student()
james.greeting()

# 클래스는 다중상속 사능 class Student(Person,University)
# 추상 클래스 : 미완성 메서드만 가지고 있는 클래스 -> 상속받은 클래스에서 완성하도록 함(모든 메서드를 상속받은 클래스에서 구현해야 오류안남)
# 또한 추상클래스는 인스턴스를 만들 수 없음 -> 그래서 추상클래스의 몸통은 pass로 미완성함함

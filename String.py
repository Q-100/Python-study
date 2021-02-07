import math

python = "Python is Amazing"
print(python.upper())  # 대문자로 반환
print(python.lower())  # 소문자로 반환:wq
print(python[0].isupper())  # 1번째 배열에 있는 문자가 대문자인지 확인(맞으면 true, 틀리면 false)
print(python.replace("Python", "java"))  # 첫번째 인자에 있는 문자열을 두번째 인자의 문자열로 치환

print(python.index("i"))  # 문자열 중 인자로 들어간 문자 또는 문자열을 검사해 첫번째로 발견된 인덱스 반환, 없을 시 오류반환
print(python.find("is"))  # 문자열 중 인자로 들어간 문자 또는 문자열을 검사해 첫번째로 발견된 인덱스 반환, 없을 시 -1반환
print(python.count("isa"))  # 입력한 문자 또는 문자열을 검사해 갯수를 반환

age = 26
color = "blue"
print(f"저는 {age}살이며 {color}색을 좋아합니다")  # 앞에 f를 붙여 format을 사용
print("저는 {}살이며 {}색을 좋아합니다..".format(26, "blue"))  # format안에 들어있는 순서대로 들어감
print("저는 {1}살이며 {1}색을 좋아합니다.".format(26, "blue"))  # format의 원하는 인덱스를 {}에 넣으면 인덱스값으로 들어감
print("저는 {name}이며 {country}에 삽니다.".format(name="민호", country="서울"))  # format에 이름을 정해줄수 있음
print("수학에서 파이 = {m.pi:.3f}입니다.".format(m=math))  # math모듈을 받아와서 사용가능(:을 이용해 자를수도있음)

print("저는 '김규백' 입니다.")
print("저는 \"김규백\"입니다.")
print("C:\\Users\\Desktop")
print("Red Apple\rPine")  # 맨앞으로 커서를 이동해서 침(Pine만 출력)
print("Redd\bApple")  # 앞글자 삭제
print("Red\t\tApple")
print("Red\nApple")

print("a", "b")  # 한칸 뛰고 출력

x = [0, 1, 2, 3, 4]
y = ["Hello", "there"]
print(x.index(3))  # 3이 들어가있는 인덱스를 반환
print("Hello" in y)  # 리스트 안에 문자열 또는 문자가 있는지 확인, 있을시 true 없을 시 false
x.append([11, 22])  # [11,22]를 리스트 맨 뒤에 추가
print(x)

print("abc" "abcd")  # 콤마 없이 문자열을 붙이면 합쳐짐
print("""안녕하세요 
저는 김규백입니다.
반갑습니다""")  # 따옴표 3개를 사용하면 \n을 사용하지 않고 멀티라인으로 작성가능

print(r"이스케이프문자\n 라인바꾸기 \\이런거 다무시함 \tㅎㅎ")  # 앞에 r을 붙이면 이스케이프 문자 모두 무시
print(",".join(y))  # 리스트내용을 앞에 구분자로 합쳐짐
a = list(map(int, "1 2 3 4".split()))  # map은 기존리스트를 건드리지 않고 새로운 map객체를 만들어냄 -> 그래서 list를 붙여서 리스트로 만들어야됨
print(a)
print(type(a[0]))

q = "1,2,3,4".split(",")
print(type(list(map(int, q))[0]))

departure, _, arrival = "seattle-Seoul".partition("-")  # partition은 구분자를 기반으로 튜플형으로 반환함(반환값이랑 저장할 변수랑 같아야함)
print(departure)
print(_)
print(arrival)

a = "abcdefg"
print(a.capitalize())  # 첫번째 문자만 대문자로하고 나머지 모두 소문자로(무조건 첫번째가 대문자됨, 공백이면 안보임), a는 안바뀜

s = "   abcd   "
print(s.strip()) # 양쪽의 공백문자를 제거, s는 안바뀜




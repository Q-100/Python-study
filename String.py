python = "Python is Amazing"
print(python.upper()) # 대문자로 반환
print(python.lower()) # 소문자로 반환:wq
print(python[0].isupper()) # 1번째 배열에 있는 문자가 대문자인지 확인(맞으면 true, 틀리면 false)
print(python.replace("Python", "java")) # 첫번째 인자에 있는 문자열을 두번째 인자의 문자열로 치환

print(python.index("i")) # 문자열 중 인자로 들어간 문자 또는 문자열을 검사해 첫번째로 발견된 인덱스 반환, 없을 시 오류반환
print(python.find("is")) # 문자열 중 인자로 들어간 문자 또는 문자열을 검사해 첫번째로 발견된 인덱스 반환, 없을 시 -1반환
print(python.count("isa")) # 입력한 문자 또는 문자열을 검사해 갯수를 반환

age = 26
color = "blue"
print(f"저는 {age}살이며 {color}색을 좋아합니다")
print("저는 '김규백' 입니다.")
print("저는 \"김규백\"입니다.")
print("C:\\Users\\Desktop")
print("Red Apple\rPine") # 맨앞으로 커서를 이동해서 침(Pine만 출력)
print("Redd\bApple") # 앞글자 삭제
print("Red\t\tApple")
print("Red\nApple")

print("a", "b") # 한칸 뛰고 출력


python = "Python is Amazing"
print(python.upper()) # 대문자로 반환
print(python.lower()) # 소문자로 반환:wq
print(python[0].isupper()) # 1번째 배열에 있는 문자가 대문자인지 확인(맞으면 true, 틀리면 false)
print(python.replace("Python", "java")) # 첫번째 인자에 있는 문자열을 두번째 인자의 문자열로 치환

print(python.index("i")) # 문자열 중 인자로 들어간 문자 또는 문자열을 검사해 첫번째로 발견된 인덱스 반환, 없을 시 오류반환
print(python.find("is")) # 문자열 중 인자로 들어간 문자 또는 문자열을 검사해 첫번째로 발견된 인덱스 반환, 없을 시 -1반환
print('tset')
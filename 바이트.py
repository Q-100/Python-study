b = b"abcde"
print(b)
print(type(b)) #타입은 문자열이 아닌 바이트임

s = b"abc def hij"
print(s.split()) # 스플릿을 해도 앞에 각각 b가 붙음
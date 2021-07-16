print("%f" % float(input()))
print("%04d.%02d.%02d" % (5, 3, 5))  # %0i는 i번째 자리에 포맷값을 넣고 나머지를 0으로채움
index = 1
fruit = "apple"
print(f"{index + 1} {fruit}")  # 리액트 문법하고 비슷함 큰따옴표 앞에 f붙이기

print("{1}{0}".format(index+1,fruit))

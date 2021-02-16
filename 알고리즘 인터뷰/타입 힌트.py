a = 1
b: str = "1"  # 이런식으로 타입에 대한 힌트를 줄 수 있음


def test(b: str) -> str:  # 이런식으로 파라미터와 리턴의 형태를 힌트를 줄 수 있음
    return b


# 하지만 힌트는 힌트일뿐 동적으로 입력이 됨

print([n * 2 for n in range(10) if n % 2 == 0])

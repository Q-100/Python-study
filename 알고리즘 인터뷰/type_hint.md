# Type Hint

## 변수 선언시 타입을 정의해주는 방법
``` python
a: int = 1 
b: str = "1"
c: list = ["apple","banana"] 
d: dict = {"key1":3,"key2":4}
```

## 함수 선언 시 파라미터에 타입을 정의해주는 방법

```python
def test(b: str) -> str:  
    return b
```
* 이런식으로 파라미터와 리턴의 형태를 힌트를 줄 수 있음
* 하지만 힌트는 힌트일뿐 `동적`으로 할당이 됨

print([n * 2 for n in range(10) if n % 2 == 0])


def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n

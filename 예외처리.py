def division(a, index):
    try:  # 실행할 식 -> 오류가 생기면 except문으로 감 -> 오류가 생기지 않을 경우 else문을 실행
        if a % 2 != 0:
            raise Exception("2의 배수를 입력하세요")  # 조건을 걸어서 조건에 맞지 않으면 밑에 Exception의 e에 오류 메시지 전달
        z = y[index] / a
    except ZeroDivisionError as e:  # 예외처리를 구분 할 수 있음(as를 이용하여 오류 메세지를 저장 할 수 있음)
        return print("0으로 나눌수는 없습니다.", e)
    except IndexError as e:
        return print("인덱스를 잘못입력하셨습니다.", e)
    except Exception as e:
        return print("오류", e)
    else:  # 오류가 발생하지 않았을 경우
        print(z)
    finally:  # 오류가 발생하든 안하든 무조건 실행
        print("종료")


y = [10, 20, 30]
index, x = map(int, input("인덱스와 나눌 숫자를 입력하세요(나눌숫자는 2의 배수만 입력하세요) : ").split())
division(x, index)

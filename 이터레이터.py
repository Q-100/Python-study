# 이터레이터 : 값을 차례대로 꺼낼 수 있는 객체
# 이터레이터는 반복가능한 객체에서 __iter__로 이터레이터를 얻고 __next__로 다음 숫자를 꺼냄
import random
it = iter(range(3))  # iter()은 __iter__를 실행(iter(호출가능한객체(매개변수없는함수또는 람다),반복을 끝낼값) 또는 iter(반복가능한객체)
print(next(it))  # next()는 __next__를 실행하여 이터레이터에서 값을 차례대로 꺼냄
print(next(it))
print(next(it))
print(next(it,10)) # next(반복가능한객체,기본값)으로 할수 있으며 반복이 끝났을 때는 오류를 출력하는게 아닌 기본값을 출력(next(it)으로하면 오류나옴)


# for i in iter(lambda: random.randint(0, 5), 2):
#     print(i)

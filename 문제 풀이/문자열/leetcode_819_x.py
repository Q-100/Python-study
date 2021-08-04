paragraph = "Bob hit a ball, BOB BOB BOB the hit BALL flew far after it was hit."
banned = ["hit"]
import re
import collections


def mostCommonWord(paragraph, banned):
    words = [word for word in re.sub(r"[\W]"," ",paragraph).lower().split() if word not in banned]
    # \W로 문자나 숫자가 아닌 내용을 모두 공백으로 바꾸고 소문자로 변환 뒤 스플릿함 -> 스플릿한 단어가 banned에 없을 경우 word 리스트에 저장
    answer = collections.Counter(words)
    # Counter 객체 사용
    return answer.most_common(1)[0][0]
    # Counter 객체의 most_common을 사용
    # 가장 많은 갯수를 가진 객체를 반환한 후 0번째에 있는 단어 출력(most_common은 (ball,2)처럼 반환되기 때문에)

print(mostCommonWord(paragraph, banned))

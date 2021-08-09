class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        # 1번째 인덱스 순으로 비교해서 정렬하되 처음에 정렬이 안될경우 0번째 인덱스 값으로 비교해서 정렬
        return letters + digits
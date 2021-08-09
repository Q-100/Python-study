nums = [2, 7, 11, 15]
target = 22


def bruteforce(nums, target):
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def use_in(nums, target):
    for i, n in enumerate(nums):
        tmp = target - n
        if tmp in nums[i + 1:]:  # 이미 방문한 인덱스는 건너뛰어야하기 때문에 i+1부터 시작
            return [i, nums[i + 1:].index(tmp) + (i + 1)]  # 방문한 인덱스 다음부터 시작, 실제 인덱스는 i+1만큼 줄었으니까 늘려줌


def dictionary_change(nums, target):
    """

    :param nums:
    :param target:
    :return: 기존 풀이들은 모두 첫번째 숫자를 타겟에서 뺀 값을 찾는데
    이 풀이는 딕셔너리에 넣는 동시에 값을 찾기 때문에 첫번째 값은 딕셔너리에 반대로 대입 후
    두번째 숫자를 뺏을 때의 값인 첫번째 값을 찾음
    그렇기 때문에 return이 tmp[target-n],i 로 나옴
    """
    tmp = {}
    for i, n in enumerate(nums):
        if target - n in tmp:
            return [tmp[target - n], i]
        tmp[n] = i


print(bruteforce(nums, target))
print(use_in(nums, target))
print(dictionary_change(nums, target))

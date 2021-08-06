nums = [2, 7, 11, 15]
target = 22


def bruteForce(nums, target):
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

def useIn(nums,target):
    for i,j in enumerate(nums):
        tmp = target-j
        if tmp in nums[i+1:]:
            return [i,nums.i]

print(bruteForce(nums,target))


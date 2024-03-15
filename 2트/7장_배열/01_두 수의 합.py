# https://leetcode.com/problems/two-sum/

# 브루트 포스 O(n^2)
def solution1(nums: list[int], target: int):
    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print(i, j)
                return


# in을 이용한 탐색 O(n)
def solution2(nums: list[int], target: int):
    for i, n in enumerate(nums):
        sub = target - n
        if sub in nums[i + 1:]:
            print(i, nums.index(sub))
    return


# 첫번째 수를 뺀 결과 키 조회 O(1)
def solution3(nums: list[int], target: int):
    dic = {}
    for i, n in enumerate(nums):
        dic[n] = i
    for i, n in enumerate(nums):
        if target-n in dic.keys():
            print(i, dic[target-n])
            return


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    solution3(nums, target)

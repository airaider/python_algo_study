#https://leetcode.com/problems/two-sum/

#브루트 포스 O(n^2)
def solution1(nums : list[int], target: int):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]

#in을 이용한 탐색 O(n)
def solution2(nums : list[int], target: int):
    for i,n in enumerate(nums):
        sum = target-n
        if sum in nums[i+1:]:
            return i, nums[i+1:].index(sum)+i+1

#첫번째 수를 뺀 결과 키 조회 O(1)
def solution3(nums : list[int], target: int):
    map={}
    for i,n in enumerate(nums):
        map[n]=i
    for i,n in enumerate(nums):
        if target-n in map and i != map[target-n]:
            return i, map[target-n]

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    solution3(nums, target)
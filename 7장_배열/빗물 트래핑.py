#https://leetcode.com/problems/trapping-rain-water/

#투포인터
def solution(height : list[int]):
    print(height)

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
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    solution(height)
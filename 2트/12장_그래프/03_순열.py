# https://leetcode.com/problems/permutations/

# Nested function, DFS
def solution(nums):
    results = []
    visit = []
    def dfs(cnt):
        if cnt == len(nums):
            results.append(visit[:])
        for i in nums:
            if i not in visit:
                visit.append(i)
                dfs(cnt+1)
                visit.pop()
    dfs(0)
    print(results)

# itertools 내장 함수
import itertools
def permut(nums):
    answer = list(itertools.permutations(nums))
    answer2 = list(map(list, itertools.permutations(nums)))
    print(answer2)


if __name__ == '__main__':
    nums = [1,2,3]
    solution(nums)
    # permut(nums)

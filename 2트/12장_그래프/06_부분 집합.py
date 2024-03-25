# https://leetcode.com/problems/combination-sum/submissions/

# 모든 원소 거치고 나온 다음에 append
def solution(nums):
    answer = []

    def dfs(path, idx):
        if idx == len(nums):
            answer.append(path[:])
            return
        dfs(path+[nums[idx]], idx+1)
        dfs(path, idx+1)
    path = []
    dfs(path, 0)
    print(answer)


# 매 iteration 나오는대로 append
def solution1(nums):
    answer = []
    def dfs(path, idx):
        answer.append(path[:])
        for i in range(idx, len(nums)):
            dfs(path+[nums[i]], i+1)

    dfs([], 0)
    print(answer)


if __name__ == '__main__':
    nums = [1,2,3]
    solution1(nums)


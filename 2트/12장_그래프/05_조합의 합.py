# https://leetcode.com/problems/combination-sum/submissions/

# Nested function, DFS
def solution(candidates, target):
    answer = []

    def dfs(sum, path, idx):
        if sum > target:
            return
        elif sum == target:
            answer.append(path[:])
        else:
            for i in range(idx, len(candidates)):
                dfs(sum + candidates[i], path + [candidates[i]], i)

    path = []
    dfs(0, path, 0)
    print(answer)


if __name__ == '__main__':
    candidates = [2,3,6,7]
    target = 7
    solution(candidates, target)


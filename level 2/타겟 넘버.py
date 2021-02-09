def solution(numbers, target):
    def dfs(sum, idx):
        ret=0
        if idx == len(numbers):
            if sum == target:
                return 1
            else: return 0

        ret+=dfs(sum+numbers[idx], idx+1)
        ret+=dfs(sum-numbers[idx], idx+1)
        return ret

    a = dfs(0,0)
    answer = 0
    print(a)

    return answer


if __name__ == '__main__':
    numbers = [1,1,1,1,1]
    target = 3
    solution(numbers, target)
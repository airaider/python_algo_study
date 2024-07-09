from programmers.util.test_runner import run_tests


def solution(numbers, target):
    def dfs(cnt, depth):
        ret = 0
        if depth == len(numbers):
            if cnt == int(target):
                return 1
            else:
                return 0
        ret += dfs(cnt + numbers[depth], depth + 1)
        ret += dfs(cnt - numbers[depth], depth + 1)
        return ret

    return dfs(0, 0)


if __name__ == "__main__":
    run_tests(solution)

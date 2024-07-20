from programmers.util.test_runner import run_tests


def solution(n, times):
    n = int(n)
    left = 1
    right = min(times) * n

    while left < right:
        mid = (left + right) // 2
        cnt = sum(mid // time for time in times)

        if cnt >= n:
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == "__main__":
    run_tests(solution)

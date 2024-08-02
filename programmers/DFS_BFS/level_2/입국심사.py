from programmers.util.test_runner import run_tests


def solution(n, times):
    n = int(n)
    left = 1
    right = n * times[-1]
    answer=0
    while left < right:
        mid = (left + right) // 2
        cnt = sum(mid//time for time in times)
        print(left, right, mid, cnt)
        if cnt >= n:
            right = mid
        else:
            left = mid + 1
    print(left)
    return left


if __name__ == "__main__":
    run_tests(solution)

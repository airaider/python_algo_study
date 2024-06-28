from programmers.util.test_runner import run_tests


def solution(nums):
    return min(len(set(nums)), len(nums) // 2)


if __name__ == "__main__":
    run_tests(solution)

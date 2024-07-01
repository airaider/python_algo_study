from programmers.util.test_runner import run_tests


def solution(nums):
    return min(len(set(nums)), len(nums) // 2)


if __name__ == "__main__":
    solution([1,2,3,4,5,6,7,8,9])
    # run_tests(solution)

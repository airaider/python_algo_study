import collections


def solution(nums):
    answer = 0
    print(len(set(nums)))
    print(len(nums) // 2)
    return min(len(set(nums)), len(nums) // 2)


if __name__ == '__main__':
    nums = [3, 3, 3, 2, 2, 2]
    solution(nums)

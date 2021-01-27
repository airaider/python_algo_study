import collections


def solution(nums, target):
    left = 0
    right = len(nums)-1

    while left<=right:
        mid = (left+right)//2

        if nums[mid]>target:
            right = mid-1
        elif nums[mid]<target:
            left = mid
        else:
            print(mid)
            return mid

    return

def solution1(nums, target):
    try:
        return nums.index(target)
    except ValueError:
        return -1

if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    target = 9
    solution(nums, target)

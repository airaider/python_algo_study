import collections


def solution(nums, target):

    left =0
    right = len(nums)-1
    while left < right:
        mid = (left + right)//2

        if nums[mid] > nums[right]:
            left = mid+1
        else:
            right = mid
    print(mid)

    pivot = nums.index(min(nums))
    print(pivot)



    return


if __name__ == '__main__':
    nums = [4,5,6,7,0,1,2]
    target = 1
    solution(nums, target)

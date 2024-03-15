def solution(nums : list[int]):
    left = []
    right = []
    p=1

    for i in range(0, len(nums)):
        left.append(p)
        p*=nums[i]
    print(left)

    p=1
    for i in range(len(nums)-1, -1, -1):
        left[i]*=p
        p*=nums[i]
    print(left)


if __name__ == '__main__':
    nums = [1,2,3,4]
    solution(nums)
def solution(nums : list[int]):
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        pair.append(n)
        if len(pair)==2:
            sum+=min(pair)
            pair = []
    print(sum)

def solution1(nums : list[int]):
    sums = 0
    pair = []
    nums.sort()

    for i,n in enumerate(nums):
        if i%2==0:
            sums+=n
    print(sums)

    sums=0
    print(sum(nums[::2]))


if __name__ == '__main__':
    nums = [1,4,3,2]
    solution1(nums)
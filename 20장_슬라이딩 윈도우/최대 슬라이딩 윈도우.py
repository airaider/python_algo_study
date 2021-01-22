import collections


def solution1(nums, k):
    r = []
    for i in range(len(nums)-k+1):
        r.append(max(nums[i:i+k]))
    print(r)
    return


def solution2(nums, k):
    current_max = float('-inf')
    window = collections.deque()
    result = []
    for i,v in enumerate(nums):
        window.append(v)
        print(window)
        if i<k-1:
            continue
        if current_max == float('-inf'):
            current_max = max(window)
        elif v>current_max:
            current_max = v

        print(current_max)
        result.append(current_max)

        if window.popleft() == current_max:
            current_max = float('-inf')

    print(result)
    return

if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k=3
    solution1(nums, k)
    solution2(nums, k)
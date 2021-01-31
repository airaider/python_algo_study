import collections
import bisect


def solution1(nums1, target):
    left, right = 0, len(nums1)-1
    while left<right:
        if nums1[left]+nums1[right]>target:
            right-=1
        elif nums1[left]+nums1[right]<target:
            left+=1
        else:
            print(left+1, right+1)
            return


def solution2(nums1, target):

    for k,v in enumerate(nums1):
        tar = target-v
        i = bisect.bisect_left(nums1, tar, k+1)
        if i<len(nums1) and nums1[i]==tar:
            print(k+1, i+1)
            return



if __name__ == '__main__':
    nums1 = [2,7,11,15]
    target = 9
    solution2(nums1, target)

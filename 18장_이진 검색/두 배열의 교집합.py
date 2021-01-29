import collections
import bisect


def solution(nums1, nums2):
    result = set()
    nums2.sort()
    print(nums2)
    for n1 in nums1:
        print(n1)
        i2 = bisect.bisect_left(nums2, n1)
        print(i2)
        print(nums2[i2])

        if len(nums2)>0 and len(nums2)>i2 and nums2[i2] == n1:
            result.add(n1)
    print(result)

    return

def solution1(nums1, nums2):
    nums1.sort()
    nums2.sort()
    print(nums1)
    print(nums2)
    result = set()
    i=j=0
    while i<len(nums1) and j<len(nums2):
        if nums1[i] == nums2[j]:
            result.add(nums1[i])
            i+=1
            j+=1
        elif nums1[i] < nums2[j]:
            i+=1
        else:
            j+=1

    print(result)

    return


if __name__ == '__main__':
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    solution1(nums1, nums2)

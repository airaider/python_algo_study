#https://leetcode.com/problems/3sum/

#투포인터
def solution(nums : list[int]):
    nums.sort()
    print(nums)
    answer = []
    for i in range(len(nums) -2):
        left, right = i, len(nums) - 1
        while left < right:
            sum = i + nums[left] + nums[right]
            if sum > 0:
                right -= 1
            elif sum < 0:
                left += 1
            else:
              answer.append([nums[i], nums[left], nums[right]])
    print(answer)



if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    solution(nums)
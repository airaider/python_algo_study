#https://leetcode.com/problems/trapping-rain-water/

#투포인터
def solution1(height : list[int]):
    print(height)

#스택 O(n)
def solution2(height : list[int]):
    print(height)
    stack = []
    volume = 0
    past = height[0]
    for i in range(len(height)):
        print(height[i])
        if height[i]>past:
            print("curve")
        past = height[i]

if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    solution2(height)
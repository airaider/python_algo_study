#https://leetcode.com/problems/daily-temperatures/

#스택
def solution(T : list[int]):
    answer = [0] * len(T)
    stack = []
    for i,t in enumerate(T):
        while stack and t > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i-last
        stack.append(i)
    print(answer)
    return True


if __name__ == '__main__':
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    solution(T)
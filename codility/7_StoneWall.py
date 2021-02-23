def solution(H):
    stack = [H[0]]
    answer = 1
    for i in range(1, len(H)):
        print(stack)
        while stack and H[i] < stack[-1]:
            stack.pop()
        if not stack or H[i] > stack[-1]:
            stack.append(H[i])
            answer+=1

    return answer


if __name__ == '__main__':
    H = [8, 8, 5, 7, 9, 8, 7, 4, 8]
    solution(H)

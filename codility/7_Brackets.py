def solution(S):
    # write your code in Python 3.6
    stack = []
    match = {'}': '{', ')': '(', ']': '['}
    print(match)
    for i in S:
        if i == '{' or i == '[' or i == '(':
            stack.append(i)
        else:
            if len(stack) == 0: return 0
            print(match[i])
            if stack[-1] != match[i]:
                return 0
            stack.pop()
    if len(stack) != 0: return 0
    return 1

    pass


if __name__ == '__main__':
    S = "{[()()]}"
    solution(S)

def solution1(s):
    stack = []
    stack.append(s[0])
    for i in s[1:]:
        print(i)
        if len(stack)>0:
            now = stack[-1]
            if now == i:
                stack.pop()
            else:
                stack.append(i)
        else: stack.append(i)
    print(len(stack))
    if len(stack): return 0
    return 1

def solution(s):
    answer = []
    for i in s:
        if not(answer):
            answer.append(i)
        else:
            if(answer[-1] == i):
                answer.pop()
            else:
                answer.append(i)
    return not(answer)


if __name__ == '__main__':
    s = 'baabaa'
    solution(s)
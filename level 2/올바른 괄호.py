def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == '(':
            stack.append()
        else:
            if len(stack)==0:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    return False


if __name__ == '__main__':
    s = '(())()'
    solution(s)
def solution(A,B):

    stack = []
    flag = B[0]
    eat = []
    for a,b in zip(A,B):
        if b == 1:
            flag = 1
            eat.append(a)
        if b == 0:
            if not flag:
                stack.append(b)
            else:
                while eat and a>eat[-1]:
                    eat.pop()
                if not eat:
                    stack.append(a)
                    flag = 0
    print(len(eat) + len(stack))
    return len(eat) + len(stack)


if __name__ == '__main__':
    A = [4,3,2,1,5]
    B = [0,1,0,0,0]
    solution(A,B)

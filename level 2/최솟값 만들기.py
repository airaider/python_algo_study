def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for a,b in zip(A,B):
        answer+=(a*b)
    print(answer)
    return answer


def solution1(A,B):
    return sum(a*b for a,b in zip(sorted(A), sorted(B, reverse=True)))


if __name__ == '__main__':
    A = [1, 4, 2]
    B = [5, 4, 4]
    solution(A,B)
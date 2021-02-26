def solution(A):
    print(A)
    if not A: return -1
    answer = []
    sum_now = -1001
    max_sum = -1001

    for i in A:
        if i < 0:
            if max_sum != -1001:
                answer.append(max_sum)
            sum_now = -1001
            max_sum = -1001
            continue
        sum_now = max(i, sum_now + i)
        max_sum = max(max_sum, sum_now)
    if max_sum >= 0: answer.append(max_sum)
    if not answer: return -1
    return max(answer)


if __name__ == '__main__':
    A = [1, 2, -3, 4, 5, -6]
    print(solution(A))
    A = [-8, 3, 0, 5, -3, 12]
    print(solution(A))
    A = [-1, 2, 1, 2, 0, 2, 1, -3, 4, 3, 0, -1]
    print(solution(A))
    A = [-1]
    print(solution(A))
    A = [2]
    print(solution(A))

    A = [-1, -1]
    print(solution(A))

    A = [0, 0, 0, 0, 0]
    print(solution(A))

    A = [0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, -1, 2]
    print(solution(A))

    A = [-1, 0, -1]
    print(solution(A))
    A = [0, -1, 0]
    print(solution(A))
    A = [0]
    print(solution(A))

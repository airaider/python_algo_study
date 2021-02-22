def solution(A, K):
    # write your code in Python 3.6

    temp = [0 for _ in range(len(A))]
    for i,v in enumerate(A):
        temp[(i+K)%len(A)] = v

    print(temp)
    pass


if __name__ == '__main__':
    A = [3, 8, 9, 7, 6]
    K = 3
    solution(A, K)
def solution(A):
    # write your code in Python 3.6
    if not A: return 0
    min = A[0]
    profit = 0
    for i in A:
        if i < min:
            min = i
        if i - min > profit:
            profit = i - min
    print(min, profit)


    pass


if __name__ == '__main__':
    A = [23171, 21011, 21123, 21366, 21013, 21367]
    solution(A)
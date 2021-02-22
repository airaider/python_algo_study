def solution(A):
    temp = [i for i in range(1, len(A)+2)]
    print(sum(temp) - sum(A))
    pass


if __name__ == '__main__':
    A = [2,3,1,5]
    solution(A)
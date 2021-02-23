def solution(A):
    # write your code in Python 3.6
    A.sort()
    print(A)
    print(A[-3] * A[-2] * A[-1])
    print(A[0] * A[1] * A[-1])
    return max(A[-3] * A[-2] * A[-1], A[0] * A[1] * A[-1])

if __name__ == '__main__':
    A = [-3,1,2,-2,5,6]
    solution(A)
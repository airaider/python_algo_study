# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # write your code in Python 3.6
    answer = B//K - A//K
    if A%K==0:
        answer+=1
    return answer


if __name__ == '__main__':
    A = 5
    B = 12
    K = 2
    solution(A, B, K)
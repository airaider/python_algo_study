# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    answer = 0
    total = sum(A)
    for i in range(len(A)):
        if A[i]==0:
            answer+=total
        else:
            total-=1
        if answer>1000000000: return -1
    print(answer)
    return answer


if __name__ == '__main__':
    A = [0,1,0,1,1]
    solution(A)
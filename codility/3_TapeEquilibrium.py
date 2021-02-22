def solution(A):
    # write your code in Python 3.6

    left = 0
    left_sum = 0
    right_sum = sum(A)
    answer = []
    while left<len(A)-1:
        left_sum+=A[left]
        right_sum-=A[left]
        answer.append(abs(left_sum-right_sum))
        left+=1
    return min(answer)


if __name__ == '__main__':
    A = [3,1,2,4,3]
    solution(A)
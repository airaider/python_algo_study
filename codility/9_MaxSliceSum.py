def solution(A):

    if len(A) == 1:
        return A[0]

    sum_now=A[0]
    max_sum=A[0]

    for i in A[1:]:

        sum_now = max(i, sum_now+i)
        max_sum = max(max_sum, sum_now)
        print(sum_now, max_sum)
    print(max_sum)
    pass


if __name__ == '__main__':
    A = [3,2,-6,4,0]
    solution(A)
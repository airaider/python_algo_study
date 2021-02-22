def solution(A, B):
    answer = 0
    A.sort()
    A.sort()

    j=0
    for i in range(len(A)):
        print(A[j], B[i])
        if A[j]<B[i]:
            answer+=1
            j+=1

    print(answer)

    return answer


if __name__ == '__main__':
    A = [5,1,3,7]
    B = [2,2,6,8]
    solution(A, B)
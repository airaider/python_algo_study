import collections

def solution(N, A):
    result = collections.defaultdict(int)
    maxVal = 0
    maxSum = 0
    for i in A:
        if i == N+1:
            maxSum+=maxVal
            result.clear()
            maxVal=0
        else:
            result[i - 1] += 1
            if result[i - 1] > maxVal:
                maxVal = result[i - 1]
    answer = [maxSum for _ in range(N)]
    for i in result.items():
        answer[i[0]]+=i[1]
    print(result)
    print(answer)
    return answer


if __name__ == '__main__':
    A = [3,4,4,6,1,4,4]
    N=5
    solution(N, A)
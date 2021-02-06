import collections

def solution(N, stages):
    answer = collections.defaultdict()
    cnt = len(stages)
    for stage in range(1, N+1):
        if cnt<=0: answer[stage]=0
        else: answer[stage]=stages.count(stage)/cnt
        cnt -= stages.count(stage)


    answer = sorted(answer, key=lambda x:answer[x], reverse=True)
    print(answer)

    return answer


if __name__ == '__main__':
    N = 5
    stages = [2, 1, 2, 6, 2, 4, 3, 3]
    solution(N, stages)
import math

def solution(progresses, speeds):
    answer = []
    task = []
    for p,s in zip(progresses,speeds):
        task.append(math.ceil((100 - p) / s))
    print(task)
    cnt = 1
    for i in range(1, len(task)):
        if task[i-cnt]>=task[i]:
            cnt+=1
        else:
            answer.append(cnt)
            cnt=1
    answer.append(cnt)
    print(answer)

    return answer


if __name__ == '__main__':
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]
    solution(progresses, speeds)
    progresses = [95, 90, 99, 99, 80, 99]
    speeds = [1, 1, 1, 1, 1, 1]
    solution(progresses, speeds)
    progresses = [99, 1, 99, 1]
    speeds = [1, 1, 1, 1]
    solution(progresses, speeds)

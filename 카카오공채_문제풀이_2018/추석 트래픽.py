import datetime

def solution(lines):
    combined_logs = []
    for line in lines:
        lines = line.split()
        timestamp = datetime.datetime.strptime(lines[0]+' '+lines[1], "%Y-%m-%d %H:%M:%S.%f").timestamp()
        combined_logs.append((timestamp,-1))
        combined_logs.append((timestamp - float(lines[2][:-1]) + 0.0001, 1))

    combined_logs.sort(key=lambda x:x[0])
    print(combined_logs)

    acc = 0
    max_request = 1

    for i, el1 in enumerate(combined_logs):
        current = acc
        for el2 in combined_logs[i:]:
            if el2[0] - el1[0] >0.999:
                break
            if el2[1] > 0:
                current+=1
        max_request = max(current, max_request)
        acc += el1[1]
    print(max_request)
    return


if __name__ == '__main__':
    lines = ['2016-09-15 20:59:57.421 0.351s', '2016-09-15 20:59:58.233 1.181s', '2016-09-15 20:59:58.299 0.8s', '2016-09-15 20:59:58.688 1.041s', '2016-09-15 20:59:59.591 1.412s', '2016-09-15 21:00:00.464 1.466s', '2016-09-15 21:00:00.741 1.581s', '2016-09-15 21:00:00.748 2.31s', '2016-09-15 21:00:00.966 0.381s', '2016-09-15 21:00:02.066 2.62s']
    solution(lines)

def solution(record):
    print(record)
    log = {}
    answer=[]
    for rec in record:
        status = rec.split()
        print(status)
        if status[0]=='Enter':
            log[status[1]]=status[2]
            answer.append((status[1], '님이 들어왔습니다.'))
        elif status[0]=='Leave':
            answer.append((status[1], '님이 나갔습니다.'))
        elif status[0]=='Change':
            log[status[1]]=status[2]
    print(log)
    print(answer)
    result=[]
    for ans in answer:
        result.append(log[ans[0]]+ans[1])
    print(result)
    return result


if __name__ == '__main__':
    record = 	["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
    solution(record)


def solution(record):
    print(record)
    answer=[]
    dict = {}
    for log in record:
        state = log.split()
        print(state)
        if state[0]=='Enter':
            dict[state[1]] = state[2]
            answer.append((state[1],"님이 들어왔습니다."))
        elif state[0] == 'Leave':
            answer.append((state[1],"님이 나갔습니다."))
        else:
            dict[state[1]] = state[2]
    print(dict)
    print(answer)
    sol = []
    for ans in answer:
        print(dict[ans[0]])
        sol.append(dict[ans[0]]+ans[1])
    print(sol)

    return


if __name__ == '__main__':
    record = 	["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
    solution(record)
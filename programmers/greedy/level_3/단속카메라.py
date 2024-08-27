def solution(routes):
    routes.sort(key=lambda x: (x[0]))
    print(routes)
    answer = 0
    while routes:
        start, end = routes.pop(0)
        answer += 1
        while routes:
            l, r = routes.pop(0)
            if l > end:
                break
            end = min(end, l)
    print(answer)

def solution1(routes):
    routes.sort(key=lambda x: x[0])
    answer = 0
    end = -30001

    for start, exit in routes:
        if start > end:
            answer += 1
            end = exit
        else:
            end = min(end, exit)
    return answer




if __name__ == '__main__':
    routes = [[-20, -15], [-14, -5], [-18, -13], [-5, -3]]
    answer = 2
    solution(routes)

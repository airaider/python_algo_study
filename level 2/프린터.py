def solution(priorities, location):
    answer = 0
    seq = []
    printer=[(i,v) for i,v in enumerate(priorities)]

    while True:
        cur = printer.pop(0)
        if any(cur[1] < q[1] for q in printer):
            printer.append(cur)
        else:
            answer+=1
            if cur[0]==location:
                return answer


if __name__ == '__main__':
    priorities =[2, 1, 3, 2]
    location = 2
    solution(priorities, location)
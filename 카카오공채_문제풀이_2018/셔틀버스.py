import collections

def solution(n,t,m,timetable):
    timetable = [
        int(time[:2])*60 + int(time[3:])
        for time in timetable
    ]
    timetable.sort()
    print(timetable)
    candidate=0
    current = 540
    for _ in range(n):
        for _ in range(m):
            print(timetable)
            print(candidate)
            if timetable and timetable[0] <= current:
                candidate = timetable.pop(0) - 1
            else:
                candidate = current
        current+=t

    print(candidate)
    h,m = divmod(candidate, 60)
    print(h,m)
    print(str(h).zfill(2)+":"+str(m).zfill(2))

    return

if __name__ == '__main__':
    n=2
    t=10
    m=2
    timetable = ["09:10", "09:09", "08:00"]
    solution(n,t,m,timetable)
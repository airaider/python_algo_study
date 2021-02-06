def solution(a, b):
    day = ['SUN', 'MON','TUE','WED','THU','FRI','SAT']
    days = [31,29,31, 30,31,30,31, 31, 30, 31, 30, 31]
    total = 0
    for i in range(a-1):
        total += days[i]
    total+=b
    idx = (5+total)%7
    return day[idx-1]


if __name__ == '__main__':
    a=5
    b=24
    solution(a,b)
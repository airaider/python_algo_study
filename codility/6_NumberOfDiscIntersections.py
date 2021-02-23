def solution(A):
    # write your code in Python 3.6

    inter = []

    for i,v in enumerate(A):
        inter.append((i-v, -1))
        inter.append((i+v, 1))

    inter.sort()
    print(inter)

    intersections = 0
    intervals = 0

    for i, v in enumerate(inter):
        if v[1] == 1:
            intervals -= 1
        if v[1] == -1:
            intersections += intervals
            intervals +=1
        print(intersections, intervals)

    return -1 if intersections > 10000000 else intersections


if __name__ == '__main__':
    A = [1,5,2,1,4,0]
    solution(A)

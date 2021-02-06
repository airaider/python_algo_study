def solution(n, lost, reserve):
    for i in range(1, n+1):
        if i in reserve and i in lost:
            reserve.remove(i)
            lost.remove(i)

    cnt = n - len(lost)
    for l in lost:
        if l+1 in reserve:
            reserve.remove(l+1)
            cnt+=1
        elif l-1 in reserve:
            reserve.remove(l-1)
            cnt+=1
    return cnt


if __name__ == '__main__':
    n = 8
    lost = [1,2,4,6]
    reserve = [1,2,4,6]
    solution(n, lost, reserve)
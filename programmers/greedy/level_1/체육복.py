def solution1(n, lost, reserve):
    for i in range(1, n + 1):
        if i in reserve and i in lost:
            reserve.remove(i)
            lost.remove(i)

    cnt = n - len(lost)
    for l in lost:
        if l + 1 in reserve:
            reserve.remove(l + 1)
            cnt += 1
        elif l - 1 in reserve:
            reserve.remove(l - 1)
            cnt += 1
    return cnt


def solution(n, lost, reserve):
    uniforms = [1] * n

    for i in reserve:
        uniforms[i - 1] += 1

    for i in lost:
        uniforms[i - 1] -= 1

    for i in range(n):
        if uniforms[i] == 0:
            if i > 0 and uniforms[i - 1] == 2:
                uniforms[i - 1] -= 1
                uniforms[i] += 1
            elif i < n - 1 and uniforms[i + 1] == 2:
                uniforms[i + 1] -= 1
                uniforms[i] += 1

    return sum(1 for u in uniforms if u > 0)


if __name__ == '__main__':
    n = 5
    lost = [2, 4]
    reserve = [1, 3, 5]
    solution(n, lost, reserve)

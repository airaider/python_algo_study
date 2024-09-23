from collections import deque


def solution(cap, n, deliveries, pickups):
    distance = 0
    cur_deliver = 0
    cur_pickup = 0
    for i in range(n - 1, -1, -1):
        cur_pickup += deliveries[i]
        cur_deliver += pickups[i]
        while cur_deliver > 0 or cur_pickup > 0:
            distance += (i + 1) * 2
            cur_deliver -= cap
            cur_pickup -= cap
    print(distance)

    return


if __name__ == '__main__':
    cap = 4
    n = 5
    deliveries = [1, 0, 3, 1, 2]
    pickups = [0, 3, 0, 4, 0]
    solution(cap, n, deliveries, pickups)

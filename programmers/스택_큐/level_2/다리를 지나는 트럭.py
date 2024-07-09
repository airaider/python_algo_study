from programmers.util.test_runner import run_tests

from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    current_weight = 0
    while trucks or current_weight > 0:
        time += 1
        current_weight -= bridge.popleft()
        if trucks and trucks[0] + current_weight <= weight:
            current_weight += trucks[0]
            bridge.append(trucks.popleft())
        else:
            bridge.append(0)
    return time


if __name__ == "__main__":
    run_tests(solution)

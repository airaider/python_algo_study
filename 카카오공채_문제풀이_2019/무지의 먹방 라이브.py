import heapq

def solution(food_times, k):
    food = [(food, idx) for idx, food in enumerate(food_times, 1)]
    heapq.heapify(food)

    small_food = food[0][0]
    prev_food = 0
    while k - ((small_food - prev_food) * len(food)) >=0:
        k -= ((small_food - prev_food) * len(food))
        prev_food, idx = heapq.heappop(food)
        if not food:
            return -1
        small_food = food[0][0]
    answer = sorted(food, key=lambda x:x[1])
    print(answer[k%len(answer)][1])

    return answer[k%len(answer)][1]


if __name__ == '__main__':
    food_times = [3,1,2]
    k = 5
    solution(food_times, k)

import collections

def solution(prices):
    answer = []
    deq = collections.deque(prices)
    print(deq)
    while deq:
        curr = deq.popleft()
        time=0
        for n in deq:
            time+=1
            if curr>n:
                break
        answer.append(time)
    print(answer)
    return answer


if __name__ == '__main__':
    prices = [1, 2, 3, 2, 3]
    solution(prices)
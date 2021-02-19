import heapq


def solution(operations):
    heap=[]
    heapq.heapify(heap)
    for op in operations:
        print(heap)
        op = op.split()
        print(op)

        if op[0] == 'I':
            heapq.heappush(heap, int(op[1]))
        else:
            if not heap: continue
            if op[1] == '1':
                heap.pop()
            else:
                heapq.heappop(heap)
    if not heap: return [0,0]
    print(max(heap), min(heap))
    return [max(heap), min(heap)]


if __name__ == '__main__':
    operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
    solution(operations)
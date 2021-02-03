import itertools


def solution(d, budget):
    d.sort()
    for i in range(len(d)):
        print(sum(d[:i+1]))
        if sum(d[:i+1])<=budget:
            continue
        else: return i
    return len(d)


def solution1(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)




if __name__ == '__main__':
    d = [2,2,3,3]
    budget = 10
    print(solution(d,budget))
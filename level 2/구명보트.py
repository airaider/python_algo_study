import collections

def solution1(people, limit):
    answer = 0
    people.sort()
    people = collections.deque(people)
    while people:
        answer+=1
        can = people.popleft()
        print(can)
        for i in people:
            if can+i<=limit:
                people.pop(i)
                break
    print(answer)

    return answer


def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    print(people)
    print(answer)
    return len(people) - answer


if __name__ == '__main__':
    people = [70, 50, 80, 50]
    limit = 100
    solution(people, limit)
from collections import defaultdict


def solution1(friends, gifts):
    given_gifts = defaultdict(lambda: defaultdict(int))
    received_gifts = defaultdict(lambda: defaultdict(int))

    for gift in gifts:
        giver, receiver = gift.split()
        given_gifts[giver][receiver] += 1
        received_gifts[receiver][giver] += 1

    gift_index = {}
    for friend in friends:
        given = sum(given_gifts[friend].values())
        received = sum(received_gifts[friend].values())
        gift_index[friend] = given - received

    next_month = defaultdict(int)
    for i, f1 in enumerate(friends):
        for f2 in friends[i + 1:]:
            g1 = given_gifts[f1][f2]
            g2 = given_gifts[f2][f1]
            if g1 > g2:
                next_month[f1] += 1
            elif g1 < g2:
                next_month[f2] += 1
            else:
                if gift_index[f1] > gift_index[f2]:
                    next_month[f1] += 1
                elif gift_index[f1] < gift_index[f2]:
                    next_month[f2] += 1

    if next_month.values():
        return max(next_month.values())
    return 0

def solution(friends, gifts):
    f = {v: i for i, v in enumerate(friends)}
    l = len(friends)
    p = [0] * l
    answer = [0] * l
    map = [[0] * l for i in range(l)]
    l = len(friends)
    print(map)
    for gift in gifts:
        giver, receiver = gift.split()
        map[f[giver]][f[receiver]] += 1
    for i in range(l):
        p[i] = sum(map[i]) - sum(k[i] for k in map)
    print(p)
    for i in range(l):
        for j in range(l):
            if map[i][j] > map[j][i]:
                answer[i]+=1
            elif map[i][j] == map[j][i]:
                if p[i] > p[j]:
                    answer[i] += 1
    print(answer)


if __name__ == '__main__':
    friends = ["muzi", "ryan", "frodo", "neo"]
    gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
    solution(friends, gifts)

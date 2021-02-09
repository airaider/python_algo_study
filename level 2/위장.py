import collections
from functools import reduce


def solution(clothes):
    answer = 0
    wear = collections.defaultdict(list)
    for clothe in clothes:
        wear[clothe[1]].append(clothe[0])
    cat=[]
    print(wear)
    a = collections.Counter([kind for name, kind in clothes])
    answer=1
    for can in a.values():
        answer*=(can+1)
    answer = reduce(lambda x,y:x*(y+1), a.values(), 1)
    print(answer-1)
    return answer-1


if __name__ == '__main__':
    clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
    solution(clothes)
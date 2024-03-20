#https://leetcode.com/problems/jewels-and-stones/

#defautdict
import collections
def solution(jewels, stones):
    print(jewels, stones)

    bag = collections.defaultdict(int)
    for s in stones:
        bag[s] += 1
    print(bag)
    money = 0
    for j in jewels:
        money+=bag[j]

    print(money)
    return True

#Counter
def solution1(jewels, stones):
    freqs = collections.Counter(stones)
    money = 0
    for j in jewels:
        money += freqs[j]
    print(money)
    return True

#list comprehension
def solution2(jewels, stones):
    print(sum(s in jewels for s in stones))

if __name__ == '__main__':
    jewels = "aA"
    stones = "aAAbbbb"
    solution2(jewels, stones)
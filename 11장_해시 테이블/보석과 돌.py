#https://leetcode.com/problems/jewels-and-stones/

#defautdict
import collections
def solution(jewels, stones):
    print(jewels, stones)

    stone = collections.defaultdict(int)
    for char in stones:
        stone[char] += 1

    total = 0
    for jewel in jewels:
        total += stone[jewel]

    print(total)
    return True

#Counter
def solution1(jewels, stones):
    freqs = collections.Counter(stones)
    print(freqs)

    count=0
    for char in jewels:
        count+=freqs[char]
    print(count)

#list comprehension
def solution2(jewels, stones):
    print(sum(s in jewels for s in stones))

if __name__ == '__main__':
    jewels = "aA"
    stones = "aAAbbbb"
    solution2(jewels, stones)
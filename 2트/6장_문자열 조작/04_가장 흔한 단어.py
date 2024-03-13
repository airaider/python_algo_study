#https://leetcode.com/problems/most-common-word/

#리스트 컴프리헨션, Counter 객체
import re
import collections
def solution(paragraph : str, banned : list[str]):

    words = [word for word in re.sub(r'\W', ' ', paragraph).lower().split() if word not in banned]
    print(words)

    counts = collections.defaultdict(int)
    for word in words:
        counts[word] += 1
    print(counts.values())
    print(max(counts.values()))

    print(max(counts, key=counts.get))

    counts = collections.Counter(words)
    print(counts)
    print(counts.most_common(1))

    print(paragraph, banned)


if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    solution(paragraph, banned)
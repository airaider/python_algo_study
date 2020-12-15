#https://leetcode.com/problems/most-common-word/

#리스트 컴프리헨션, Counter 객체
import re
import collections
def solution(paragraph : str, banned : list[str]):
    print(paragraph, banned)
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
    print(words)
    counts = collections.defaultdict(int)
    for word in words:
        counts[word]+=1
    print(max(counts, key=counts.get))

    counts = collections.Counter(words)
    #counts.most_common(1)이 가장 흔하게 등장한 첫번째 값
    print(counts.most_common(1)[0][0])


if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    solution(paragraph, banned)
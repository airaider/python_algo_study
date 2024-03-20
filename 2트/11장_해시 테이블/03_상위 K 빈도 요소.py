#https://leetcode.com/problems/longest-substring-without-repeating-characters/

#힙 que
import collections
import heapq
def solution(nums, k):
    freqs = collections.Counter(nums)
    print(freqs)
    answer = []
    freqs_heap = []
    for f in freqs:
        heapq.heappush(freqs_heap, (-freqs[f], f))
    print(freqs_heap)
    for _ in range(k):
        answer.append(heapq.heappop(freqs_heap)[1])
    print(answer)

#Counter 내장 함수
def solution1(nums, k):
    freqs = collections.Counter(nums)
    a = [k[0] for k in freqs.most_common(k)]
    print(a)

if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    k = 2
    solution1(nums, k)
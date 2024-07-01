# from programmers.util.test_runner import run_tests
from collections import defaultdict


def solution(clothes):
    clothes_dict = defaultdict(int)
    for i, j in clothes:
        clothes_dict[j] += 1
    answer = 1
    for i in clothes_dict.values():
        answer *= (i+1)
    return answer - 1


if __name__ == "__main__":
    clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    answer = 5
    solution(clothes)

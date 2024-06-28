from programmers.util.test_runner import run_tests
import collections


def solution(participant, completion):
    a = collections.Counter(participant)
    b = collections.Counter(completion)
    c = a - b
    return list(c.keys())[0]


if __name__ == "__main__":
    run_tests(solution)

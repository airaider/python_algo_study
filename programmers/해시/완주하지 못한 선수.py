from programmers.util.test_runner import run_tests
import collections


def solution1(participant, completion):
    a = collections.Counter(participant)
    b = collections.Counter(completion)
    c = a - b
    return list(c.keys())[0]


def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i, e in enumerate(completion):
        if e != participant[i]:
            return participant[i]
    return participant[-1]


if __name__ == "__main__":
    solution1([1, 2, 3, 5], [1, 2, 3, 4])
    # run_tests(solution)

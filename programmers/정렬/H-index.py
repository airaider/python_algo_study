from programmers.util.test_runner import run_tests


def solution(citations):
    citations.sort(reverse=True)
    for i, v in enumerate(citations):
        if i + 1 > v:
            return i
    return len(citations)


if __name__ == "__main__":
    run_tests(solution)

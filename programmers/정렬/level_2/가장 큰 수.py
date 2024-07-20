from programmers.util.test_runner import run_tests

import functools
def solution(numbers):
    num = list(map(str, numbers))

    def compare(a, b):
        t1 = a + b
        t2 = b + a
        return (int(t1) > int(t2)) - (int(t1) < int(t2))

    num.sort(key=functools.cmp_to_key(compare), reverse=True)
    answer = ''.join(num)
    return '0' if answer[0] == '0' else answer


if __name__ == "__main__":
    run_tests(solution)

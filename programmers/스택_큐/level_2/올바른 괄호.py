from programmers.util.test_runner import run_tests


def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
            # stack.pop(0) 0번 pop은 O(n) 소모
    return len(stack) == 0


if __name__ == "__main__":
    run_tests(solution)
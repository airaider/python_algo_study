from programmers.util.test_cases import test_cases


def run_tests(solution_func):
    for i, test in enumerate(test_cases, 1):
        result = solution_func(**test["input"])
        if result == test["expected"]:
            print(f"Test case {i} passed")
        else:
            print(f"Test case {i} failed. Expected {test['expected']}, but got {result}")

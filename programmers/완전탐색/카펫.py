from programmers.util.test_runner import run_tests

import math


def solution(brown, yellow):
    area = brown + yellow
    for i in range(3, math.floor(math.sqrt(area)) + 1):
        if area % i == 0:
            width = i
            height = area // i
            y_width = width - 2
            y_height = height - 2
            if y_width * y_height == yellow:
                return [height, width]


if __name__ == "__main__":
    run_tests(solution)

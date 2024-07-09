from programmers.util.test_runner import run_tests


def solution(people, limit):
    print(people, limit)
    limit = int(limit)
    people.sort()
    left, right = 0, len(people)-1
    answer = 0
    while left <= right:
        boat = people[left] + people[right]
        if boat <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        answer += 1
    return answer


if __name__ == "__main__":
    run_tests(solution)

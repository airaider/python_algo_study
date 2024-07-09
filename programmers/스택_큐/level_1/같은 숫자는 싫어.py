from programmers.util.test_runner import run_tests


def solution(arr):
    ans = []
    temp = arr[0]
    ans.append(temp)
    for i in arr:
        if i == temp:
            continue
        else:
            ans.append(i)
            temp = i
    return ans


def solution1(arr):
    answer = []
    prev = -1
    for a in arr:
        if a != prev:
            answer.append(a)
        prev = a
    return answer


if __name__ == "__main__":
    run_tests(solution)

from programmers.util.test_runner import run_tests


def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True


if __name__ == "__main__":
    run_tests(solution)

from datetime import datetime
from collections import defaultdict


def solution1(today, terms, privacies):
    today = today.split(".")

    today_date = datetime(int(today[0]), int(today[1]), int(today[2]))

    term_dict = defaultdict()
    for term in terms:
        kind, end = term.split(" ")
        term_dict[kind] = end

    answer = []

    for i, privacy in enumerate(privacies):
        check_date, kind = privacy.split()
        year = int(term_dict[kind]) // 12
        month = int(term_dict[kind]) % 12
        check_date = check_date.split(".")
        if int(check_date[1]) + month > 12:
            year += 1
            month -= 12
        check_date = datetime(int(check_date[0]) + year, int(check_date[1]) + month, int(check_date[2]))
        print(check_date, today_date)
        if check_date > today_date:
            answer.append(i)
    print(answer)
    return answer


def solution(today, terms, privacies):
    year = 28 * 12
    month = 28

    y, m, d = map(int, today.split("."))
    today_day = year * y + month * m + d

    term_dict = {kind: int(end) for kind, end in (term.split(" ") for term in terms)}

    answer = []
    for i, privacy in enumerate(privacies):
        check_date, kind = privacy.split()
        y, m, d = map(int, check_date.split("."))
        date_day = year * y + month * m + d
        date_day += term_dict[kind] * month
        if today_day >= date_day:
            answer.append(i + 1)
    print(answer)
    return answer


if __name__ == '__main__':
    today = "2020.01.01"
    terms = ["Z 3", "D 5"]
    privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
    # solution(today, terms, privacies)

    today = "2022.05.19"
    terms = ["A 6", "B 12", "C 3"]
    privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
    solution(today, terms, privacies)

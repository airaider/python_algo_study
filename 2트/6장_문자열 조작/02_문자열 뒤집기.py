#투 포인터
def solution1(s : list[str]):
    print(s)

#파이썬 내장 함수
def solution2(s : list[str]):
    print(s)
    print(s[::-1])
    s.reverse()
    print(s)

if __name__ == '__main__':
    solution1(["h", "e", "l", "l", "o"])
    solution1(["H", "a", "n", "n", "a", "h"])
    solution2(["h", "e", "l", "l", "o"])
    solution2(["H", "a", "n", "n", "a", "h"])
import collections

def solution(n):
    point = collections.Counter(bin(78))['1']
    while True:
        n+=1
        if point==collections.Counter(bin(n))['1']:
            print(n)
            return n


if __name__ == '__main__':
    n = 78
    solution(n)
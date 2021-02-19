import itertools

def solution(n, k):
    answer = []
    people = [i for i in range(1, n+1)]
    print(people)
    a = itertools.permutations(people, n)


    for i in a:
        print(i)
    return answer


if __name__ == '__main__':
    n = 3
    k = 5
    solution(n,k)
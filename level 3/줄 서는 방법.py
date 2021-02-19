import math

def solution(n, k):
    answer = []
    people = [i for i in range(1, n+1)]
    print(people)

    while n!=0:
        fact = math.factorial(n-1)
        answer.append(people.pop((k-1)//fact))
        print(fact)
        n=n-1
        k%=fact
    print(answer)
    return answer


if __name__ == '__main__':
    n = 3
    k = 5
    solution(n,k)
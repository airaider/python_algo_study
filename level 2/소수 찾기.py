import itertools


def solution(numbers):

    def prime(n):
        if n==1:
            return False
        if n==2 or n==3:
            return True
        if n>2:
            limit = int(n**(1/2))
            for i in range(2, limit + 1):
                if n % i == 0:
                    return False
            return True

    answer = 0
    nums = set()

    for i in range(len(numbers)):
        for p in itertools.permutations(list(numbers),i+1):
            nums.add(int(''.join(p)))
    print(nums)

    for n in nums:
        if prime(n): answer+=1
    print(answer)
    return answer


if __name__ == '__main__':
    numbers = '011'
    solution(numbers)
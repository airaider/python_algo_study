import itertools

def solution(nums):
    answer = 0

    def prime(n):
        limit = int(n**(1/2))
        for i in range(2, limit+1):
            if n%i==0: return False
        return True

    nums.sort()
    for i in itertools.combinations(nums, 3):
        print(i)
        print(sum(i))
        if prime(sum(i)):
            answer+=1
    print(answer)
    return answer


if __name__ == '__main__':
    nums = [1,2,7,6,4]
    solution(nums)
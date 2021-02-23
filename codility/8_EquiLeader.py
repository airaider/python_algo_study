import collections


def solution(A):
    left = collections.defaultdict(int)
    right = collections.defaultdict(int)

    for a in A:
        right[a]+=1
    print(right)
    answer = 0

    l_max = 0

    for i in A[:-1]:
        left[i]+=1
        # if i
        right[i]-=1
        if right[i]==0:
            del right[i]
        print(left, right)
        if max(left.keys()) == max(right.keys()):
            print(i)
            answer+=1
    print(answer)
    return answer


if __name__ == '__main__':
    A = [4,3,4,4,4,2]
    solution(A)

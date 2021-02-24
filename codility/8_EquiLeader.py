import collections


def solution(A):
    left = collections.defaultdict(int)
    right = collections.defaultdict(int)

    for a in A:
        right[a]+=1
    print(right)
    answer = 0

    l_max = 0
    l_cnt = 0
    for i in A[:-1]:
        left[i]+=1
        # if i
        right[i]-=1
        if right[i]==0:
            del right[i]

        if left[i]>l_cnt:
            l_max = i
            l_cnt = left[i]

        if l_cnt>len(left)/2 and right[l_max]>len(right)/2:
            print(i)
            answer+=1

    print(answer)
    return answer


def solution(A):
    count = 0

    right_dict = {}
    right_len = len(A)
    for a in A:
        if a in right_dict:
            right_dict[a] += 1
        else:
            right_dict[a] = 1

    left_leader = 0
    left_leader_count = 0
    left_dict = {}
    left_len = 0

    for a in A:

        right_dict[a] -= 1
        right_len -= 1

        if a in left_dict:
            left_dict[a] += 1
        else:
            left_dict[a] = 1
        left_len += 1

        if left_dict[a] > left_leader_count:
            left_leader = a
            left_leader_count = left_dict[a]

        if left_leader_count > left_len / 2 and right_dict[left_leader] > right_len / 2:
            count += 1

    return count


if __name__ == '__main__':
    A = [4,3,4,4,4,2]

    solution(A)

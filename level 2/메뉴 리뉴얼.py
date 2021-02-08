import itertools
import collections

def solution(orders, course):
    result=[]

    for c in course:
        answer = collections.defaultdict(int)
        for order in orders:
            order=sorted(order)
            for i in itertools.combinations(order, c):
                food = ''.join(i)
                answer[food]+=1
        max_val = max(answer.values())
        if max_val<2: break

        answer = sorted(answer.items(), key=lambda x:x[1], reverse=True)
        print(answer)

        for candidate in answer:
            if candidate[1]==max_val:
                result.append(candidate[0])
            else: break
    print(result)
    result=sorted(result)
    print(result)
    return answer


if __name__ == '__main__':
    orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    course = [2,3,4]
    solution(orders, course)
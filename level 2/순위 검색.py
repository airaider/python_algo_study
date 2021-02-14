import collections
import bisect


def solution(info, query):
    answer = []
    info_dict = collections.defaultdict(list)
    print(info)

    def search(nums, target):
        return len(nums) - bisect.bisect_left(nums, target)

    for data in info:
        data = data.split()
        score = int(data[-1])

        temp = []
        temp.append(data[0])
        temp.append('-')
        idx = 1
        while len(temp) < 16:
            size = len(temp)
            for _ in range(size):
                a = temp.pop(0)
                temp.append(a + data[idx])
                temp.append(a + '-')
            idx += 1
        for t in temp:
            info_dict[t].append(score)
    for key in info_dict.keys(): info_dict[key].sort()
    print(info_dict)

    for q in query:
        q = q.split()
        score = int(q[-1])
        _q = ''
        for i in q[:-1]:
            if i != 'and':
                _q += i
        print(q)
        print(_q)
        print(info_dict[_q])
        cnt = search(info_dict[_q], score)
        answer.append(cnt)

    print(answer)
    return answer


if __name__ == '__main__':
    info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
            "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
             "cpp and - and senior and pizza 250", "- and backend and senior and - 150",
             "- and - and - and chicken 100", "- and - and - and - 150"]
    solution(info, query)

def solution(files):
    answer = []
    storage=[]
    for idx, file in enumerate(files):
        print(file)
        head=''
        number=''
        flag=1
        for i in range(len(file)):
            if file[i].isdigit():
                flag=0
                number+=file[i]
            else:
                if not flag:
                    break
                head+=file[i]
        storage.append((idx, head.lower(), int(number)))
        print(head, number)
    print(storage)
    storage.sort(key=lambda x:(x[1], x[2], x[0]))
    print(storage)
    for s in storage:
        answer.append(files[s[0]])
    print(answer)
    return answer


import re

def solution1(files):
    a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
    return b


if __name__ == '__main__':
    files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
    solution(files)
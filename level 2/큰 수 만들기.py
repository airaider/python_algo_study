def solution2(number, k):
    limit = len(number)-k
    answer=''
    while limit and number:
        if len(number)==1:
            answer+=number
            break
        if limit==1:
            find = number[:]
        else:
            find = number[:-(limit-1)]
        a = max(find)
        answer+=a
        number=number[number.index(a)+1:]
        limit-=1
    print(answer)
    return answer


def solution1(number, k):
    results = []
    lenNumber = len(number)
    lenResult = lenNumber - k
    th = -1
    for i in range(lenResult):
        val = "0"
        for j in range(th+1, lenNumber -(lenResult - len(results))+1):

            if val < number[j]:
                th = j
                val = number[j]
                if val == "9": break
        results.append(val)
    answer = "".join(results)
    return answer


def solution(number, k):
    stack = [number[0]]
    print(stack)
    for num in number[1:]:
        print(stack)
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    print(stack)
    return ''.join(stack)


if __name__ == '__main__':
    number = '1231234'
    k=3
    solution(number, k)
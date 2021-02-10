def solution(numbers, hand):
    answer = ''
    l = [3, 0]
    r = [3, 1]
    key = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    for num in numbers:
        print(num)
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
            l = key[num]
        elif num == 3 or num == 6 or num == 9:
            answer += 'R'
            r = key[num]
        else:
            dis_l = abs(key[num][0] - l[0]) + abs(key[num][1] - l[1])
            dis_r = abs(key[num][0] - r[0]) + abs(key[num][1] - r[1])
            if dis_l < dis_r:
                answer += 'L'
                l = key[num]
            elif dis_r < dis_l:
                answer += 'R'
                r = key[num]
            else:
                if hand == 'right':
                    answer += 'R'
                    r = key[num]
                else:
                    answer += 'L'
                    l = key[num]

    print(answer)

    return answer


if __name__ == '__main__':
    numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand = 'right'
    solution(numbers, hand)

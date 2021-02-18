def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[0])
    print(routes)

    while routes:
        car = routes.pop(0)
        print(car)
        limit = car[1]
        answer+=1
        while routes:
            i = routes[0]
            print(i, limit)
            if i[0]>limit:
                break
            limit = min(limit, i[1])
            routes.pop(0)
    print(answer)
    return answer


if __name__ == '__main__':
    routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
    solution(routes)
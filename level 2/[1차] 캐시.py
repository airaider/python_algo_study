import collections

def solution(cacheSize,cities):
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            time+=1
            cache.remove(city)
            cache.append(city)
        else:
            time+=5
            cache.append(city)
    print(time)
    return

if __name__ == '__main__':
    cacheSize = 3
    cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']
    solution(cacheSize,cities)
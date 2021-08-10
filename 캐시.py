def solution(cacheSize, cities):
    cache =[''] * cacheSize

    time = 0
    for city in cities:
        if city.lower() in cache:
            time += 1
        else:
            time += 5
            cache.append(city.lower())
            cache.pop(0)

    return time
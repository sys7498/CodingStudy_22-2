def solution(cacheSize, cities):
    cache = []
    if (cacheSize == 0):
        return len(cities)*5

    for i in range(cacheSize):
        cache.append(['', 0])

    lru = 1
    lruIndex = 0
    answer = 0
    for k in cities:
        print(k)
        for i in range(len(cache)):
            cache[i][1] += 1

        for i in range(len(cache)):
            if cache[i][1] > lru:
                lru = cache[i][1]
                lruIndex = i

        for i in range(len(cache)):
            if (cache[i][0] == k.lower()):
                print(i, ' 번째 index hit!')
                cache[i][1] = 1
                answer += 1
                print("+1")
                break
            else:
                if (cache[i][0] == ''):
                    print("cold miss")
                    cache[i][0] = k.lower()
                    cache[i][1] = 1
                    answer += 5
                    print("+5")
                    break
                if (cache[i][0] != '' and i == cacheSize-1):
                    print('miss')
                    cache[lruIndex][0] = k.lower()
                    cache[lruIndex][1] = 1
                    answer += 5
                    print("+5")
                    break
                else:
                    continue
        lru = 1

    return answer


print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju",
      "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))

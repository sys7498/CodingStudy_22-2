def solution(cacheSize, cities):
    #선입선출
    #cache hit : 참조하고자하는 메모리가 캐시에 존재하는 경우
    #cache miss : 참조하고자하는 메모리가 캐시에 존재하지 않는 경우
    cache = []
    time = 0
    for city in cities:
        city = city.lower() #소문자로 변경
        if cacheSize >= 1:
            if not city in cache: #hit인지 miss인지 판별
                if len(cache) == cacheSize: #miss일때 길이가 같은가
                    cache.pop(0) #더이상 cashe에 저장할 용량이 없으므로 첫번째값 제거
                cache.append(city) # cache에 city 저장
                time += 5
            else: #cache hit인 경우 이전에 같은 이름의 city가 존재하므로
                cache.pop(cache.index(city)) #cache에 있던 city 삭제
                cache.append(city)
                time += 1
        else: #cache에 저장불가능->cache miss 발생
            time += 5
    return time
def solution(clothes):
    answer = 0
    hash_map = {}
    for clothe, type in clothes: #옷을 종류별로 살기
        hash_map[type] = hash_map.get(type, 0)+1
        
    print(hash_map)
    answer =1 #입지 않는 경우 계산하여 조합
    for type in hash_map:
        answer *= (hash_map[type] + 1)
        
    return (answer -1) #아무 옷도 안입는 경우 제외
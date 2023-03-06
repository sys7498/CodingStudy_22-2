def solution(clothes):
    ta = {}
    answer = 1
    for i in clothes:
        if (ta.get(i[1], None) == None):
            ta[i[1]] = 1
        else:
            ta[i[1]] += 1
    for i in ta.values():
        answer *= (i + 1)
    answer -= 1
    return answer


print(
    solution([["yellow_hat", "headgear"], ["blue_sunglasses",
                                           "eyewear"], ["green_turban", "headgear"]]))

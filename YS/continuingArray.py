def solution(elements):
    temp = []
    temp.extend(elements)
    temp.extend(elements)
    sol = []
    a = 0
    for k in range(len(elements)):
        for i in range(len(elements)):
            a += temp[k + i]
            sol.append(a)
        a = 0
    result = list(set(sol))
    return result


solution([7, 9, 1, 1, 4])

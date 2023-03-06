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
    return len(set(sol))


solution([7, 9, 1, 1, 4])

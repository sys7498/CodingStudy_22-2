def solution(brown, yellow):
    answer = []
    comb = []
    size = brown + yellow
    for i in range(1, size+1):
        if(size % i == 0):
            comb.append([i, size // i])

    for r, c in comb:
        if(r-2>0 and c-2 >0):
            y = (r-2) * (c-2)
            b = size - yellow
            if(b == brown and y == yellow):
                return [c, r]
    return False
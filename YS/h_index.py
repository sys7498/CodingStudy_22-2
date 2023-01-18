def solution(citations):
    finish = max(citations)
    maxH = 0
    for i in range(0, finish):
        bigger = 0
        lower = 0
        for item in citations:
            if (item < i):
                lower += 1
            else:
                bigger += 1
        if (bigger >= i and lower <= i):
            maxH = max(maxH, i)
    return maxH


solution([3, 0, 6, 1, 5])

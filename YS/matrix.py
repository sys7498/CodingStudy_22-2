def solution(arr1, arr2):
    fm = len(arr1)
    fn = len(arr1[0])
    sm = len(arr2)
    sn = len(arr2[0])
    answer = [[0 for p in range(sn)] for o in range(fm)]
    row = 0
    t = 0
    for i in range(fm * sn):
        a = 0
        for l in range(fn):
            a += (arr1[row][l] * arr2[l][t])
        answer[row][t] = a
        t += 1
        if (t == sn):
            row += 1
            t = 0
    return answer


print(solution([[1, 2, 3], [4, 5, 6]],
      [[1, 4], [2, 5], [3, 6]]))

# 1 1 1 1   1 1
# 1 1 1 1   1 1
#           1 1
#           1 1      
#

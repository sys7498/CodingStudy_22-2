def solution(arr1, arr2):
    r = len(arr1) #행
    c = len(arr2[0]) #열

    answer = [[0] * c for _ in range(r)]

    for i in range(r): #모든 원소를 순차적으로 곱해서 더하기
        for j in range(c):
            for k in range(len(arr1[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]

    return answer
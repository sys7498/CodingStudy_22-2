def solution(n):
    answer = 0
    value = 0
    for i in range (1, n+1): #작은 값부터 하나씩 더함
        for j in range(i, n+1):
            value += j
            if value == n:
                answer += 1
            elif value > n: #n보다 크면 break로 다음 위 for문으로 이동
                value = 0
                break
    return answer

print(solution(15))

def solution(n):
    answer = 1
    while n != 1:
        if n % 2 == 0: #2로 나눴을때 나머지가 0이면
            n /= 2 #건전지 소모가 없으므로 나누어준다
        else:
            answer += 1
            n -= 1
    return answer
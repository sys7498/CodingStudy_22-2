def solution(num):
    if num==1: #1과 2 경우는 음수가 되버려서 정의
        return 1
    if num==2:
        return 2
    answer = solution(num-1)+solution(num-2) #피보나치수열
    
    return answer%1234567
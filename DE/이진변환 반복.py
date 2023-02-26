def solution(x):
    answer = []
    
    cnt = 0 #이진변환을 수행한 횟수
    zero = 0 #삭제한 0의 개수를 셀 변수
    
    while True:
        if x == '1': #x가 '1'이면 중단
            break
        zero = zero + x.count("0") # 0의 개수를 구해서 zero에 더하기
        x = x.replace("0", "") #x에서 0을 지워준다
        
        x = bin(len(x))[2:] #x의 길이를 이진수로 변환한 문자열을 다시 x에 넣어줌 
        
        cnt = cnt + 1
    
    answer = [cnt, zero]
    
    return answer

a = "110010101001"
b = "01110"
print(solution(a))
print(solution(b))
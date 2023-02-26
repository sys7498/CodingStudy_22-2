import math

def solution(progresses, speeds):
    n = len(progresses)
    date = []
    answer = []
    
    for i in range(n):
        left_date = 100 - progresses[i]
        mok = math.ceil(left_date / speeds[i]) #반올림
        date.append(mok)
    
    while date:
        num = date.pop(0)
        result = 1 #기본값
        while len(date) != 0 and num >= date[0]:
            result += 1
            date.pop(0)
            
        answer.append(result)
        
    
    
    return answer
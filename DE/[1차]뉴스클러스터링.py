def solution(str1, str2):
    
    set1, set2 = [], []
    for i in range(len(str1)-1):
        str1_temp = str1[i] + str1[i+1]
        if str1_temp.isalpha():
            set1.append(str1_temp.lower())
            
    for j in range(len(str2)-1):
        str2_temp = str2[j] + str2[j+1]
        if str2_temp.isalpha():
            set2.append(str2_temp.lower())
      
    gyo = 0
    set2_temp = set2.copy()
    for k in set1:
        if k in set2_temp:
            gyo += 1
            set2_temp.remove(k)
    hap = len(set1) + len(set2) - gyo
    
    if hap == 0:
        answer = 1*65536
    else:
        answer = int(gyo * 65536 / hap)

        
    return answer
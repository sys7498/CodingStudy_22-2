def solution(s):
    answer = []
    s_list = s[2:-2].split('},{')
    #print(s_list)
    
    sorted_list = sorted(s_list, key=lambda x:len(x))
    #print(sorted_list)
    
    for l in sorted_list:
        ls = l.split(',')
        #print(ls)
        
        answer.append(list(set(ls)-set(answer))[0]) 
        #set 데이터타입으로 캐스팅 {} string
        #print(answer)    
        
    answer = [int(i) for i in answer]   
    
    return answer
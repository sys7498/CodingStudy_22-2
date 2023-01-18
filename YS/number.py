def solution(n):
    answer = 0
    tempa = []
    for i in range(n):
        tempa.append(i+1)
    i = 0
    k = 1
    while(i<n):
        if(sum(tempa[i:k]) < n):
            k += 1
        elif(sum(tempa[i:k]) == n):
            answer += 1
            i += 1
            k = i + 1
        else:
            i += 1
            k = i + 1
    return answer

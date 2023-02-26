def solution(numbers, target): #BFS
    answer = 0
    leaves = [0]
    for num in numbers:
        tmp = []
        for parent in leaves:  #더하고 뺀 값 수평적으로 추가
            tmp.append(parent + num)
            tmp.append(parent - num) 
        leaves = tmp #모든 계산 결과가 나오게끔
    for leaf in leaves:
        if leaf == target:
            answer += 1
    return answer
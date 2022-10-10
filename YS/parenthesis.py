def solution(s):
    answer = True
    queue = []
    
    for item in s:
        if(item == '('):
            queue.append(item)
        elif(item == ')'):
            if(len(queue) == 0):
                return False
            else:
                queue.pop()
                
    if(len(queue) == 0):
        return True
    else:
        return False

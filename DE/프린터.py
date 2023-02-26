from collections import deque
def solution(priorities, location):
    index_list = deque([i for i in range(len(priorities))])
    print(index_list)
    answer = 0
    maximum = max(priorities)
    
    while True:
        index = index_list.popleft()
        if priorities[index] < maximum:
            index_list.append(index)
        else:
            answer += 1
            priorities[index] = 0
            maximum = max(priorities)
            if index == location:
                return answer
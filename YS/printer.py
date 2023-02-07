global temp
global prio
global loc
global ans



def findBigger(number):
    global temp
    global prio
    global loc
    global ans
    if (len(temp) == 0):
        return -1
    if (len(temp) == number):
        a = temp.pop(0)
        ans += 1
        if (loc == a):
            return 1
        else:
            return -1
    elif (prio[temp[0]] < prio[temp[number]]):
        temp.append(temp.pop(0))
        return -1
    elif (prio[temp[0]] >= prio[temp[number]]):
        return findBigger(number + 1)


def solution(priorities, location):
    global temp
    global prio
    global loc
    global ans
    prio = []
    ans = 0
    prio.extend(priorities)
    temp = [i for i in range(len(priorities))]
    loc = location
    while (True):
        a = findBigger(1)
        if (a == 1):
            return ans


print(solution([2, 1, 3, 2], 2))

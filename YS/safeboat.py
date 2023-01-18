from collections import deque

def solution(people, limit):
    '''numOfBoat = 0
    boatIsNew = 0
    i = 0
    boatLimit = limit
    people.sort()
    while (i != len(people)):
        if (people[i] <= boatLimit):
            if (boatIsNew == 0):
                print("new")
                numOfBoat += 1
                boatIsNew = 1
            boatLimit -= people[i]
            i += 1
        else:
            boatLimit = limit
            boatIsNew = 0

    return numOfBoat
        for i in people:
        if (i <= boatLimit):
            if (boatIsNew == 0):
                numOfBoat += 1
                boatIsNew = 1
            boatLimit -= i
        else:
            boatIsNew = 0
            numOfBoat += 1
            boatLimit = limit - i'''

    people.sort()
    numOfBoat = 0
    while (len(people) != 0):
        if (len(people) == 1):
            people.pop()
            numOfBoat += 1
        elif (people[0] + people[-1] > limit):
            people.pop()
            numOfBoat += 1
        else:
            people.pop()
            people.pop(0)
            numOfBoat += 1
    return numOfBoat


print(solution([70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70], 100))

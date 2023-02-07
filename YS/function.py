def solution(progresses, speed):
    num = []
    answer = []
    lastIndex = 0
    for i in progresses:
        num.append(i)
    while (lastIndex != len(progresses)):
        number = 1
        for i in range(len(progresses)):
            num[i] += speed[i]
        for i in range(lastIndex, len(progresses)):
            if (num[i] >= 100):
                number += 1
                if (i == len(progresses)-1):
                    lastIndex = i+1
                    answer.append(number-1)
            else:
                if (num[lastIndex] < 100):
                    break
                else:
                    lastIndex = i
                    answer.append(number-1)
                    break

    return answer


print(solution([93, 30, 55], [1, 30, 5]))

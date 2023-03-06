global numberarray
global targetnumber
global answer
answer = 0


def solution(numbers, target):
    global numberarray
    global targetnumber
    global answer

    numberarray = numbers
    targetnumber = target
    bfs(0, 0)
    return answer


def bfs(now, sol):
    global numberarray
    global targetnumber
    global answer

    if (now == len(numberarray)):
        if (sol == targetnumber):
            answer += 1
        return sol
    else:
        bfs(now + 1, sol + numberarray[now])
        bfs(now + 1, sol - numberarray[now])


print(solution([4, 1, 2, 1], 2))

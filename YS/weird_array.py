def solution(numlist, n):
    answer = []
    for i in numlist:
        print(answer)
        if (len(answer) == 0):
            answer.insert(0, i)
        else:
            for start in range(len(answer)):
                if (abs(i - n) < abs(answer[start] - n)):
                    answer.insert(start, i)
                    break
                elif (abs(i - n) == abs(answer[start] - n)):
                    if (i > answer[start]):
                        answer.insert(start, i)
                    else:
                        answer.insert(start+1, i)
                    break
                else:
                    if (start == (len(answer) - 1)):
                        answer.append(i)
                    continue
    return answer


print(solution([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11], 6))

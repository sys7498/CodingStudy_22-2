def dfs(array, now, end, res, number, target):
    if (now == end):
        if (res == target):
            number += 1
            return number
    else:
        dfs(array, now + 1, end, res - array[now], number + 1, target)
        dfs(array, now + 1, end, res + array[now], number + 1, target)


def solution(numbers, target):
    answer = 0
    return dfs(numbers, 0, len(numbers), 0, answer, target)


print(solution([1, 1, 1, 1, 1], 3))

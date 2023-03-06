import math


def isPrimenumber(x):
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


def solution(n, k):
    a = n
    answer = 0
    string = ''
    while (a > 0):
        string = (str(a % k)) + string
        a = a // k
    array = string.split('0')
    for a in array:
        if (a == '' or a == '1'):
            continue
        if (isPrimenumber(int(a))):
            answer += 1
    return answer


print(solution(437674, 3))

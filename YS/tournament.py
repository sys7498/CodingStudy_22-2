def solution(n, a, b):
    r = 1
    while (a/2 != 0):
        if (a % 2 != 0):
            a = (a+1) / 2
        else:
            a = a / 2
        if (b % 2 != 0):
            b = (b+1) / 2
        else:
            b = b / 2

        if (a == b):
            return r
        r += 1
    return False

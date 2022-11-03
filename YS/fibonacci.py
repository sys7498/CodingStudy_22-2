import sys
sys.setrecursionlimit(10**7)
def f(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    if(n>=2):
        return f(n-1) % 1234567 + f(n-2) % 1234567

def solution(n):
    return f(n) % 1234567

print(solution(5))
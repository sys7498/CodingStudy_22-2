def toBinary(n):
    if(n == 1):
        return '1'
    return toBinary(n//2) + str(n % 2)

def solution(n):
    num = n
    orig = toBinary(n)
    while(True):
        num += 1
        bigger = toBinary(num)
        if(orig.count('1') == bigger.count('1')):
            return num
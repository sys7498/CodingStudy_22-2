def change(string, times, zero):
    if(string == '1'):
        return string, times, zero
    else:
        n = 0
        for c in string:
            if(c == '1'):
                n += 1
        zero = len(string) - n + zero
        s = ''
        while(divmod(n, 2)[0] != 0):
            s = str(divmod(n, 2)[1]) + s
            n = divmod(n, 2)[0]
        s = str(divmod(n, 2)[1]) + s
        times += 1
        return change(s, times, zero)

def solution(s):    
    times = 0
    zero = 0
    result = change(s, times, zero)
    return [result[1], result[2]]
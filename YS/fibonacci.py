def solution(n):
    fibo = []
    a = 2
    fibo.append(0)
    fibo.append(1)
    while(a <= n):
        fibo.append(fibo[a-1] % 1234567+fibo[a-2] % 1234567)
        a += 1
    return fibo[n] % 1234567
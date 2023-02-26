# 2개 수의 최소공배수 구하는 함수
def least(a, b): #유클리드 호제법
    A, B = a, b
    while b > 0:
        a, b = b, a % b 
        
    GCD = a # 최대공약수
    return A * B // GCD #몫을 사용하여 최소공배수

# arr에서 앞 2개씩 접근하면서 최소공배수 갱신
def solution(arr):
    arr.sort()
    temp = arr[0]
    for i in range(0, len(arr)-1):
        temp = least(temp, arr[i+1])
    return temp
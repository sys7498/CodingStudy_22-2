def solution(s):
    answer = ''
    lista = s.split()
    listInt = []
    for i in lista:
        listInt.append(int(i))
    listInt.sort()
    print(listInt)
    answer = answer + str(listInt[0]) + ' ' + str(listInt[len(listInt)-1])
    return answer

print(solution("-1 -2 -3 -4"))
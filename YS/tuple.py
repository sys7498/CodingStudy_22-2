def solution(s):
    temp = []
    answer = []
    for i in range(len(s)):
        if (s[i] == '{' or s[i] == '}'):
            temp.append(i)

    for i in range(len(temp)-1):
        answer.append(s[temp[i]+1:temp[i+1]])

    while '' in answer:
        answer.remove('')
    while ',' in answer:
        answer.remove(',')

    temp = []
    for i in answer:
        temp.append(i.split(','))

    temp.sort(key=len)

    sol = []
    for i in temp:
        sol.extend(list(set(i) - set(sol)))

    an = []
    for i in sol:
        an.append(int(i))
    return an


print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))

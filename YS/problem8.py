def solution(s):
    answer = ''
    s = s.lower()
    s = s.title()
    strlist = s.split()
    for i in strlist:
        if(i.isalpha() == False):
            i = i.replace(i[1],chr(ord(i[1])+32))
        answer = answer + i + ' '
    return answer.rstrip()

print(solution("3hElLo MYY nAmE isS Y"))

map = {
    '[': ']',
    '{': '}',
    '(': ')'
}


def find(s, num, answer):
    if (num == len(s) or len(s) <= 1):
        return answer
    else:
        a = []
        for i in s:
            if (i == '[' or i == '{' or i == '('):
                a.append(i)
            else:
                if (len(a) == 0):
                    return find(s[1:] + s[0], num+1, answer)
                elif (map[a[-1]] == i):
                    a.pop()
        if (len(a) == 0):
            print(s)
            return find(s[1:] + s[0], num+1, answer+1)
        else:
            return find(s[1:] + s[0], num+1, answer)


def solution(s):
    return find(s, 0, 0)


print(find("[]))}}", 0, 0))

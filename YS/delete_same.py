def solution(s):
    #if(len(s) == 0):
    #    return 1
    #else:
    #    index = 0
    #    str = ''
    #    while(index < len(s)):
    #        
    #        if(index == len(s)-1):
    #            str = str + s[index]
    #            if(len(s) == len(str)):
    #                return 0
    #            return solution(str)
    #        if(s[index] != s[index + 1]):
    #            str = str + s[index]
    #            index += 1
    #        else:
    #            str = str + s[index+2:]
    #            return solution(str)

    stack = []
    if(s == ''):
        return 0
    else:
        for i in range(len(s)):
            if(len(stack) == 0):
                stack.append(s[i])
            else:
                if(stack[-1] == s[i]):
                    stack.pop()
                else:
                    stack.append(s[i])
        if(len(stack) != 0):
            return 0
        else:
            return 1


print(solution('cdcd'))
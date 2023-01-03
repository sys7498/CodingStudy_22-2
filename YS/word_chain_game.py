def solution(n, words):
    people = []
    person = 0
    rot = 1
    for idx in range(len(words)):
        if (idx == 0):
            people.append(words[idx])
            person += 1
        elif (words[idx] in people or words[idx-1][-1] != words[idx][0]):
            return [person+1, rot]
        else:
            people.append(words[idx])
            if (person == n-1):
                person = 0
                rot += 1
            else:
                person += 1
    return [0, 0]

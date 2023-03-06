def solution(array):
    array.sort(key=lambda x: len(x))
    for i in array:
        i.replace(" ", "")
    for i in array[1:]:
        print(i)
        if (array[0] == i[0:len(array[0])]):
            return False

    return True


print(solution(["97674223", "119", "1195524421"]))

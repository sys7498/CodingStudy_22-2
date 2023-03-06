# def solution(n, left, right):
#     temp = []
#     index = 0
#     t = []
#     # answer = []
#     for p in range(n):
#         t = temp[index * n: index*n + n]
#         for k in range(n):
#             if (len(temp) <= n):
#                 temp.append(k)
#             else:
#                 if (index >= k):
#                     temp.append(t[k] + 1)
#                     if (len(temp) >= right+1):
#                         return temp[left: right+1]
#                 else:
#                     temp.append(t[k])
#                     if (len(temp) >= right+1):
#                         return temp[left: right+1]
#                 # if (len(temp) - 1 >= left):
#                 #     print(len(temp)-1)
#                 #     answer.append(temp[-1])
#                 #     if (len(temp) == right+1):
#                 #         print(len(temp)-1)
#                 #         return answer
#         index += 1

def solution(n, left, right):
    temp = [(j+1) for j in range(n)]
    index = 0
    t = []
    for p in range(n):
        t = temp[index * n: index*n + n]
        for k in range(n):
            if (index >= k):
                temp.append(t[k] + 1)
                if (len(temp) >= right+1):
                    return temp[left: right+1]
            else:
                temp.append(t[k])
                if (len(temp) >= right+1):
                    return temp[left: right+1]

        index += 1


print(solution(3, 2, 5))

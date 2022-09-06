record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

def solution(record):
    answer = []
    recordSplit = []
    uidDic = {}
    
    for item in record:
        recordSplit.append(item.split())
    
    for item in recordSplit:
        if(len(item) == 3):
            if((item[1] in uidDic) == False):
                uidDic[item[1]] = item[2]
            else:
                del uidDic[item[1]]
                uidDic[item[1]] = item[2]

    for item in recordSplit:
        if(len(item) == 2):
            answer.append(uidDic[item[1]] + "님이 나갔습니다.")
        elif(len(item) == 3):
            if(item[0] == "Enter"):
                answer.append(uidDic[item[1]] + "님이 들어왔습니다.")

    return answer
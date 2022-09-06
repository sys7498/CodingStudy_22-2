def solution(record):
    answer = []
    id_value = {}
    
    for str in record:
        strlist = str.split() 
        # split 사용해서 공백을 구분하여 배열에 넣음
        command = strlist[0]
        if command == "Enter" or command == "Change":
            id = strlist[1] 
            name = strlist[2] 
            id_value[id] = name 
            # id를 인수로 잡아서 name을 줌
            # id에 해당하는 최종 name이 저장됨       
            
    for str in record: 
        # 채팅방에 남을 메시지를 출력하기 위한 for문
        strlist = str.split()
        command = strlist[0]
        
        # Enter와 Leave만 출력하면 됨.
        if command == "Enter": 
            id = strlist[1]
            answer.append(id_value[id] + "님이 들어왔습니다.")
        elif command == "Leave":
            id = strlist[1]
            answer.append(id_value[id] + "님이 나갔습니다.")
   
    return answer
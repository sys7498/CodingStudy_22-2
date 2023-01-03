# 로또 번호 -> 1 2 3 4 5 6 + 7
def printNumOfWin(lottoList, winner, money):
    win = []                                    #가진 로또 각각 몇개숫자가 1등과 동일한지 저장(0번부터 시작)
    serviceWin = []                             #가진 로또 각각 서비스가 맞았는지 저장 (인덱스는 위에와 동일하게 생각)
    winHistory = [0, 0, 0, 0, 0, 0]             #각 등수가 몇번 당첨됐는지 저장(0번째 인덱스가 1등)
    for i in lottoList:                         #가진 로또 각각에 대하여 검사
        win.append(0)                           #로또 하나 검사할때마다 win에 추가
        serviceWin.append(0)                    #마찬가지로 서비스도 serviceWin에 추가
        for k in i[:6]:                         #
            for t in winner[:6]:                #2중for문 돌면서 각각 비교
                if (k == t):                    #같은 숫자 있다면
                    win[-1] += 1                #이번 로또에 맞은 갯수 + 1
        if (i[-1] == winner[-1]):               #서비스번호 검사
            serviceWin[-1] = 1                  #맞다면 추가
    for i in range(len(win)):                   #당첨된 갯수 확인
        if (win[i] == 6):                       #1등
            money += 1000000000
            winHistory[0] += 1
        elif (win[i] == 5 & serviceWin[i] == 1):#2등
            money += 50000000
            winHistory[1] += 1
        elif (win[i] == 5 & serviceWin[i] == 1):#3등
            money += 50000000
            winHistory[2] += 1
        elif (win[i] == 5 & serviceWin[i] == 0):#4등
            money += 1000000
            winHistory[3] += 1
        elif (win[i] == 4):                     #5등
            money += 50000
            winHistory[4] += 1
        elif (win[i] == 3):                     #6등    
            money += 5000
            winHistory[5] += 1

    #출력
    print(
        f"1등: {winHistory[0]}개\n2등: {winHistory[1]}개\n3등: {winHistory[2]}개\n4등: {winHistory[3]}개\n5등: {winHistory[4]}개\n6등: {winHistory[5]}개")
    print(f"현재 돈은 {money}원 입니다.")

    #혹시 필요할 수도 있으니 return 해놓고 나중에 필요하면 바로 쓰면됨
    return win, serviceWin, winHistory


if (__name__ == "__main__"):
    #현재가진돈
    money = 0
    #현재 가진 로또
    lottoList = [
        [2, 5, 6, 7, 3, 10, 7],
        [2, 5, 6, 7, 3, 10, 7],
        [2, 5, 6, 7, 3, 10, 7],
        [1, 2, 5, 10, 45, 32, 3],
        [2, 5, 6, 7, 3, 11, 7],
        [1, 2, 3, 4, 5, 6, 7]
    ]
    #1등로또번호
    winner = [1, 2, 3, 4, 5, 6, 7]
    #함수호출
    printNumOfWin(lottoList, [1, 2, 3, 4, 5, 6, 7], money)

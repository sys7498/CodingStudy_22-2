#picture
picture = [[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]]

#방문여부 표시용 2차원리스트
visited = [[False, False, False, False], [False, False, False, False], [False, False, False, False], [False, False, False, False], [False, False, False, False], [False, False, False, False]]


global size #전역변수 size => 한 영역의 사이즈를 표시해줌  => 영역이 새로운 영역인지, 한번 갔었던 영역인지 알려줌
size = 1 #size를 1로 초기화 

def check(picture, c, r, m, n):
    global size
    visited[c][r] = True

    # 한칸 위의 픽셀의 값을 비교(상)
    if(r-1 >= 0 and picture[c][r-1] == picture[c][r] and visited[c][r-1] == False):
        size += 1
        check(picture, c, r-1, m, n)
        
    # 한칸 아래의 픽셀의 값을 비교(하)
    if(r+1 < n and picture[c][r+1] == picture[c][r] and visited[c][r+1] == False):
        size += 1
        check(picture, c, r+1, m, n)

    # 한칸 왼쪽의 픽셀의 값을 비교(좌)
    if(c-1 >= 0 and picture[c-1][r] == picture[c][r] and visited[c-1][r] == False):
        size += 1
        check(picture, c-1, r, m, n)

    # 한칸 오른쪽의 픽셀 값을 비교(우)
    if(c+1 < m and picture[c+1][r] == picture[c][r] and visited[c+1][r] == False):
        size += 1
        check(picture, c+1, r, m, n)

    else:
        return 0

def solution(m, n, picture):
    global size
    number_of_area = 0
    max_size_of_one_area = 0
    for c in range(m):
        for r in range(n):
            check(picture, c, r, m, n)
            if(picture[c][r] != 0):
                max_size_of_one_area = max(max_size_of_one_area, size)
                if(size != 1):
                    number_of_area += 1
            size = 1
    
    print(visited)
    print(number_of_area)
    print(max_size_of_one_area)

solution(6, 4, picture)
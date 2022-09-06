picture = [[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]]
visited = [[False, False, False, False], [False, False, False, False], [False, False, False, False], [False, False, False, False], [False, False, False, False], [False, False, False, False]]

global size
size = 1

def check(picture, c, r, m, n):
    global size
    visited[c][r] = True

    if(r-1 >= 0 and picture[c][r-1] == picture[c][r] and visited[c][r-1] == False):
        size += 1
        check(picture, c, r-1, m, n)
        
    if(r+1 < n and picture[c][r+1] == picture[c][r] and visited[c][r+1] == False):
        size += 1
        check(picture, c, r+1, m, n)

    if(c-1 >= 0 and picture[c-1][r] == picture[c][r] and visited[c-1][r] == False):
        size += 1
        check(picture, c-1, r, m, n)

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
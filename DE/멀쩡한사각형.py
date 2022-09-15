w = 8
h = 12

def gcd(w, h): 
    return h if w == 0 else gcd((h % w), w)

def solution(w,h):
    return(w * h - w - h + gcd(w, h))


print(w * h - w - h + gcd(w, h))




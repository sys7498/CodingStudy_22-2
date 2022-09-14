import math

def line(x, w, h):
    y = (h/w)*x
    return y
    
def solution(w,h):
    num = 0
    for x in range(w):
        num += math.ceil(line((x+1), w, h)) - math.floor(line(x, w, h))
    return (w*h) - num
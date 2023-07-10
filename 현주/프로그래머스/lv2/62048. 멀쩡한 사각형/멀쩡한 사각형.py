from math import ceil
def GCD(x,y):
    while(y):
        x, y= y, x%y
    return x
def solution(w,h):
    answer=w * h - (w+h-GCD(w,h))
    return answer
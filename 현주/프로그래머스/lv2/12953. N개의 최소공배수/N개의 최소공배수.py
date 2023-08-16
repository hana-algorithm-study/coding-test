import math
def LCM(a, b):
        return a * b // math.gcd(a, b)
def solution(arr):
    answer = 0
    
    n=arr[0]
    for i in arr[1:]:
        n=LCM(n,i)
    return n
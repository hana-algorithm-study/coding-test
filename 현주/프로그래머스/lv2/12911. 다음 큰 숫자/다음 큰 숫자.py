from collections import Counter
def solution(n):
    answer = 0
    
    countOne=bin(n).count("1")
    
    for i in range(n+1,2*n+1):
        if bin(i).count("1")==countOne:
            answer=i
            return answer
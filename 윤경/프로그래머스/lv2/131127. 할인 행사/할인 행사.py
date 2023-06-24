# 1. 10일 간 want에 있는 게 전부 있는지 확인
# 2. number 개수만큼 있는지 확인

from collections import Counter

def solution(want, number, discount):
    answer = 0    
    tenDay = []
    join = False
    
    for i in range(len(discount)-9):
        tenDay = discount[i:i+10]
        tenDayCount = Counter(tenDay)
        
        for j in range (len(want)):
            if want[j] not in tenDay:
                join = False
                break
            if tenDayCount[want[j]] < number[j]:
                join = False
                break
            
            join = True
        
        if join == True:
            answer += 1
        
    return answer
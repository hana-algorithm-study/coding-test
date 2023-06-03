# 1-1. reserve 리스트 값이 lost에 있는지 확인
# 1-2. 있으면 둘다 지우기
# 2-1. reserve 앞 뒤 값이 lost에 있는지 확인
# 2-2. lost에서 지우기
# 3. n에서 lost길이 빼면 return 값

import copy

def solution(n, lost, reserve):
    answer = 0
    
    reserveTmp = []
    lostTmp = []
    
    reserveTmp = copy.deepcopy(reserve)
    lostTmp = copy.deepcopy(lost)
    
    lost.sort()
    reserve.sort()
    
    for i in range(len(reserveTmp)):        
        
        if reserveTmp[i] in lostTmp:
            reserve.remove(reserveTmp[i])
            lost.remove(reserveTmp[i])
    
    for x in reserve:
        if x-1 > 0 and x-1 in lost:
            lost.remove(x-1)
        elif x+1 <= n and x+1 in lost:
            lost.remove(x+1)
    answer = n-len(lost)
    
    return answer
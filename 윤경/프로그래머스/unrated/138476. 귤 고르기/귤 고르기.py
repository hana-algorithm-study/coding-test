from collections import Counter
from itertools import combinations

def solution(k, tangerine):
    answer = 0
    dict = Counter(tangerine)    # 귤 크기에 따른 개수 찾기
    
    value = list(dict.values())    # 개수만 저장하는 배열
    value.sort(reverse =True)
    sum = 0
    idx = 0
    
    while sum < k:    # 개수가 k일 때까지
        
        if k <= value[idx]:
            sum += k
        else:
            sum += value[idx]
        answer += 1    # 서로 다른 개수
        idx += 1
        
    return answer
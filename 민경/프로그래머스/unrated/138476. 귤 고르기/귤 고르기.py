from collections import Counter
def solution(k, tangerine):
    result = 0
    cnt = 0
    
    for i,j in Counter(tangerine).most_common(k) :
        result += j
        cnt += 1
        
        if result >= k :
            return cnt
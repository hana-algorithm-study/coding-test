from collections import Counter

def solution(k, tangerine):
    answer = 0
    cnt=0
    arr={}
    
    arr=Counter(tangerine)
    values = sorted(arr.values(), reverse=True)
    for i in values:
        cnt+=i
        answer+=1
        if k<=cnt:
            break
    return answer
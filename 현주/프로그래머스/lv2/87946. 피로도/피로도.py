from itertools import permutations
def solution(k, dungeons): #현재 피로도, [최소필요, 소모량]
    answer = 0
    
    for permute in permutations(dungeons, len(dungeons)):
        count=0
        hp=k
        for per in permute:
            if(hp>=per[0]):
                hp-=per[1]
                count+=1
            if count>answer:
                answer=count
                
    return answer
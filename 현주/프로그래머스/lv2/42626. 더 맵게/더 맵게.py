import heapq
def solution(scoville, K):
    answer = 0
    
    scoville.sort()
    heapq.heapify(scoville)
    now=scoville[0]
    if now >=K:
        return answer
    else:
        while(True):
            if len(scoville) == 1:
                return -1
            
            a=heapq.heappop(scoville)
            b=heapq.heappop(scoville)
            heapq.heappush(scoville,a+b*2)
            answer+=1
            
            if(scoville[0]>= K):
                return answer
                break
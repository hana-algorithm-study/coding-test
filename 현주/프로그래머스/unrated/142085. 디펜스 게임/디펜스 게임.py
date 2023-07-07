import heapq
def solution(n, k, enemy): #병사, 무적권 개수, 적
    answer = 0
    h=[]
    e=0
    
    for i in range(len(enemy)):
        e+=enemy[i]
        heapq.heappush(h,-enemy[i]) #최대 힙
        if e>n:
            if k==0:
                return i
            e+=heapq.heappop(h)
            k-=1
    
    return i+1
from collections import deque
def solution(bridge_length, weight, truck_weights):
    time=0
    waiting=deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])
    bridgeweight=0
    
    while len(waiting) or bridgeweight>0:
        go=bridge.popleft()
        bridgeweight-=go
        
        if len(waiting) and waiting[0]+bridgeweight<=weight:
            new=waiting.popleft()
            bridgeweight+=new
            bridge.append(new)
        else:
            bridge.append(0)
        time+=1
    return time
        
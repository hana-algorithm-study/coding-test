from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    on = [0 for _ in range(bridge_length)]   # 다리 위에 있는 트럭
    t = 0
    sumOn = 0   # sum() 시간 주의
    
    while len(on) > 0:
        time += 1
        tmp = on.pop(0)   # 1개 빼기
        sumOn -= tmp
        
        if len(truck_weights) > 0:
            if sumOn + truck_weights[0] > weight:
                on.append(0)
            else:
                t = truck_weights.pop(0)
                sumOn += t
                on.append(t)
                
    return time
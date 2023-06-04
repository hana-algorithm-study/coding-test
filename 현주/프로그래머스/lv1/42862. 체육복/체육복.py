def solution(n, lost, reserve):
    answer=0
    reserve1=set(reserve)-set(lost)
    lost1=set(lost)-set(reserve)
    
    for i in reserve1:
        if (i-1 in lost1):
            lost1.remove(i-1)
            answer+=1
            continue
        elif(i+1 in lost1):
            lost1.remove(i+1)
            answer+=1
    answer=n-len(lost1)
    return answer
from collections import deque
def solution(priorities, location):
    answer = 1
    q=deque(priorities)
    idx=location
    while len(q)>1:
        temp=q.popleft()
        print(q)
        if temp<max(q): #location 줄여가며 해당 값 찾기
            q.append(temp)
            if idx==0:
                idx=len(q)-1
            else:
                idx-=1
        else:
            if idx==0:
                return answer
            else:
                answer+=1
                idx-=1
                
    return answer
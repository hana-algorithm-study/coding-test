from collections import deque
def solution(cacheSize, cities):
    answer = 0
    stack=deque([])
    
    c = [i.lower() for i in cities]
    if cacheSize==0:
        return 5*len(cities)
    else:
        for i in c:
            if i not in stack:
                stack.append(i)
                answer+=5
                if len(stack) > cacheSize:
                    stack.popleft()
            else:
                stack.remove(i)
                stack.append(i)
                answer+=1
                if len(stack) > cacheSize:
                    stack.popleft()
    return answer
                
    return answer
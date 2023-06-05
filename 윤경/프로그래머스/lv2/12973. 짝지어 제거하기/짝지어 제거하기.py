def solution(s):
    answer = -1
    stack = []
    
    if len(s) %2 ==1:
        answer = 0
        return answer
    
    for x in s:
        if len(stack) == 0:
            stack.append(x)
        elif stack[-1] == x:    # 같으면
            stack.pop()
        else:
            stack.append(x)
    
    # 스택 비었으면 성공
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0   

    return answer
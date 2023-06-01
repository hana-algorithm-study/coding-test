def solution(s):
    answer = -1
    stack=[]
    #for문으로 하나씩 보면서 어떠한 배열에 push를 하는데 그 배열의 마지막과 현재 for문에 걸린 값이 같으면 배열에서 pop 아니라면 push를 하면 됩니다
    for i in s:
        if len(stack)==0:
            stack.append(i)
        else:
            if (stack[-1]==i):
                stack.pop()
            else:
                stack.append(i)
                
    if len(stack)==0:
        answer=1
    else:
        answer=0
    
    return answer
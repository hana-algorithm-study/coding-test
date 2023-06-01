from itertools import permutations
from collections import deque
def solution(expression):
    answer = 0
    ops = ["*", "+", "-"]
    
    list1 = []
    s = 0
    for i, v in enumerate(expression):
        if v in ["*", "+", "-"]:
            list1.append(expression[s:i])
            list1.append(v)
            s = i + 1
    else:
        list1.append(expression[s:])
    
    primarity = permutations(ops) #6가지의 연산자 우선순위 조합
    
    for cases in primarity:
        stacks = [deque(list1), deque()]
        t1 = 1
        for case in cases: # 각 경우에서 연산자 처리
            t1 = (t1+1) % 2
            t2 = (t1+1) % 2
            while len(stacks[t1]):
                item = stacks[t1].popleft()
                if len(stacks[t2]) and stacks[t2][-1] == case:
                    case = stacks[t2].pop()
                    n = stacks[t2].pop()
                    item = str(eval(str(n)+case+str(item)))
                stacks[t2].append(item)
            
        result = stacks[1].pop()
        result = abs(int(result))
        answer = max(answer, result)
            
    return answer
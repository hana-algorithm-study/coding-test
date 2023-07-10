from collections import deque
def solution(elements):
    answer = 0
    result=set()
    elementLen=len(elements)
    elementss=elements*2

    for i in range(1, elementLen+1): #길이 1-5
        for j in range(elementLen): #인덱스 0부터 길이만큼
            result.add(sum(elementss[j:j+i]))

    answer=len(result)
    return answer
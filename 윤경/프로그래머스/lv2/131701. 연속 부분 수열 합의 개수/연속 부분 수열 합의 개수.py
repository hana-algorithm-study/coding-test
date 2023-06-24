from itertools import combinations

def solution(elements):
    answer = 0
    extendElements = elements + elements
    result = set()
    
    for i in range(len(extendElements)):
        for j in range(1, len(elements)+1):
            tmp = sum(extendElements[i:i+j])
            result.add(tmp)
    
    answer = len(result)
    return answer         
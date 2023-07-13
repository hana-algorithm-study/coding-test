def solution(elements):
    l = len(elements)
    elements += elements
    answer = set()
    for f in range(l):
        for s in range(1, l):
            answer.add(sum(elements[f:f+s]))
            
    return len(answer)+1 
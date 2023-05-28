from itertools import product
def solution(word):
    answer = 0
    possible = []
    
    for i in range(1,6) :
        for w in product(['A', 'E', 'I', 'O', 'U'], repeat = i) :
            possible.append(''.join(list(w)))
    
    possible.sort()
    answer = possible.index(word) + 1
    
    return answer
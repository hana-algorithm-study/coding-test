from itertools import product
def solution(word):
    answer = 0
    
    word_list=[]
    for i in range(1, 6):
        for j in product([ 'A', 'E', 'I', 'O', 'U'], repeat=i):
            word_list.append(''.join(list(j)))
    word_list.sort()
    answer=word_list.index(word) + 1   
    return answer
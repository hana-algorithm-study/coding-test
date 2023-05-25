from itertools import product
def solution(word):
    answer = 0
    dict = []
    item = ['A','E','I','O','U']
    
    for i in range(1, 6):
        tmp = list(map(''.join, product(item, repeat=i)))
        dict += tmp
    
    dict.sort()
    answer= dict.index(word)+1
    return answer
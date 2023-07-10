from collections import Counter
def solution(want, number, discount):
    answer = 0
    
    dicPre = { name:value for name, value in zip(want, number) }
    
    for i in range(len(discount)-9):
        if dicPre==Counter(discount[i:i+10]):
            answer+=1
    return answer
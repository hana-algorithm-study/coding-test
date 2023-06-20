def solution(brown, yellow): #가로 >=세로
    answer = []
    
    size=brown + yellow
    for i in range(size+1,1,-1): 
        if size%i==0: 
            other=size/i 
            if (i-2) * (other - 2) == yellow:
                return [i,other]
            
            
    
    return answer
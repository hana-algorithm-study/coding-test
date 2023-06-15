import numpy as np
def solution(data, col, row_begin, row_end):
    answer = 0
    
    arr=sorted(data, key=lambda x: (x[col-1], -x[0]))
    S_i=[]
    for i in range(row_begin, row_end+1):
        result=0
        for j in arr[i-1]:
            result+=(j%i)
        answer^=result
    return answer
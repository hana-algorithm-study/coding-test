def solution(A,B):
    answer = 0
    idx, sum = 0, 0
    
    length = len(A)
    A.sort()
    B.sort(reverse = True)
    
    while idx < length:
        idx += 1
        
        mini = A[0]
        maxi = B[0]
        
        sum += mini * maxi
        
        A.remove(mini)
        B.remove(maxi)
    answer = sum
    return answer
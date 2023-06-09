def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True) #반대로
    
    for i in range(len(A)):
        A_i=A[i]
        B_i=B[i]
        answer+=A_i*B_i
    return answer
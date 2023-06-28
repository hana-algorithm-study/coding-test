def solution(n):
    answer = 0
    sum=0
    result=0
    
    array = [i for i in range(1,n+1)] #1~15
    end=0
    for start in range(n): #0부터
        while(sum<n and end<n):
            sum+=array[end]
            end+=1
        if(sum==n):
            result+=1
        sum-=array[start]
    answer=result
    return answer
    
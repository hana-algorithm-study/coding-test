def solution(n): #k칸 점프, 현재까지 거리*2로 순간이동
    ans = 0
    battery=0
    now=0
    
    while(n>0):        
        if n%2==0:      
            n=n/2  
        elif n%2==1:      
            n-=1
            battery+=1      
    ans=battery
    return ans
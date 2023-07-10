def jjack(num):
    if(num%2==0):
        return True
    else:
        return False
    
def solution(n,a,b): #n명 a,b 번호
    result=0
    while(True):
        if jjack(a)==False:
            a=(a+1)/2
        else:
            a=a/2
        if jjack(b)==False:
            b=(b+1)/2
            result+=1
        else:
            b=b/2
            result+=1
        if(a==b):
            break
    return result
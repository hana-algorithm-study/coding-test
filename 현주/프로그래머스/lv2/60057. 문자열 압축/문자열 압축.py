def solution(s):
    result=[]
    if len(s)==1:
        return 1
    
    for i in range(1, len(s)+1):
        b = ''
        cnt = 1
        tmp=s[:i]

        for j in range(i, len(s)+i, i): #1부터
            if tmp==s[j:i+j]:#앞과 같다면
                cnt+=1
            else:
                if cnt!=1: #중복이 있었다면
                    b = b + str(cnt)+tmp
                else:
                    b = b + tmp #중복 없으므로 문자열만 더하기
                    
                tmp=s[j:i+j]
                cnt = 1
                
        result.append(len(b))
        

    return min(result)
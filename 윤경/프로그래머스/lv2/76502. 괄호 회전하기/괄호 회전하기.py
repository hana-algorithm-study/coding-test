def solution(s):
    answer = -1
    cnt = 0
    
    for i in range(len(s)):          
        tmp = s
        
        for j in range(int(len(tmp)/2)):
            if "()" in tmp:
                tmp = tmp.replace('()','')
            elif "{}" in tmp:
                tmp = tmp.replace('{}','')
            elif "[]" in tmp:
                tmp = tmp.replace('[]','')
            
        if len(tmp) == 0:
            cnt += 1
        
        s = s[1:] + s[0]
    
    answer = cnt
    return answer
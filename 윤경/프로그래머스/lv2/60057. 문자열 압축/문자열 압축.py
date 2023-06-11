def solution(s):
    answer = len(s)
    
    # 문자열 중간까지만 돌리기
    for i in range(1, len(s)//2+2):
        
        cnt = 1    # 돌렸을 때 같은 것 나오는 개수
        before = s[:i]    # 단위가 될 문자열
        result = ''    # 결과 값
        
        for j in range(i, len(s)+i, len(before)):    # 맨 마지막까지 고려하기 위해 len(s)+i까지            
            after = s[j:j+i]    # 단위랑 비교할 문자열
            
            if before == after:
                cnt += 1
            
            else:
                if cnt == 1:    # 같은 게 없었다는 것이므로 result에 바로 이어주기
                    result += before
                else:
                    result += (str(cnt) + before)    
                    
                before = s[j:j+i]    # 이전 before랑 다른 값이 before가 됨
                cnt = 1    # cnt 초기화
                
        answer = min(len(result), answer)
        
    return answer
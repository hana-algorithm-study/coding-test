def solution(progresses, speeds):
    
    answer = []
    day = []
    
    for i in range(len(progresses)):
        cnt = 0
        tmp = progresses[i]
        
        # 100 될 때까지 만들기
        while tmp < 100:
            tmp += speeds[i]
            cnt += 1
        day.append(cnt)
    
    cnt = 1
    firstDay = day[0]   # 첫번째 걸리는 날짜
    
    for i in range(1, len(day)):
        # 앞 기능이 완료되지 않아 배포 못 함
        if firstDay >= day[i]:
            cnt += 1
        else:
            answer.append(cnt)
            
            firstDay = day[i]   # 다음 날짜
            cnt = 1 # 초기화
    
    answer.append(cnt)
        
    return answer
def solution(sequence, k):
    answer = [0, len(sequence)-1]    # 길이 짧은 수열 찾기 위해 초기값 넣어두기
    
    l, r = 0, 0    # 왼쪽, 오른쪽 index
    sum = 0
    
    for l in range(0, len(sequence)):
        
        # sum에 sequence[r-1]까지는 더해져 있음
        while sum < k and r < len(sequence):
            
            sum += sequence[r]
            r += 1
        
        # 길이 짧은 수열로
        if sum == k and r-1-l < answer[1]-answer[0]:
            answer = [l, r-1]    # 마지막에 r에 1 더해줬으니, answer에는 -1 해서 넣기
        
        sum -= sequence[l]   # for문 반복하면 l이 +1 부터 계산하므로 sum에서 빼주기
        
    return answer
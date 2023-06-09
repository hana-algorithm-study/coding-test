def solution(n, words):
    answer = []
    user = [[] for _ in range(n)]  # user수 길이의 list 만들기

    user_order = 0  # 마지막 사람 다음에 다시 1번으로 가기 위함
    user_cnt = 0    # 몇번째 사람이 걸렸는지
    order_cnt = 0   # 몇번째 순서에서 걸렸는지
    
    for i in range(len(words)):
        
        user_order += 1
        
        # 마지막 사람이면 다시 1번으로
        if user_order == n+1:
            user_order = 1
        
        last = words[i][-1]
        
        tmp = words[0:i]
        
        # 글자 수 1 이상 or 
        # 앞 사람이 말한 단어의 마지막 문자로 시작하는지 or 
        # 이전에 등장하지 않은 단어인지        
        if i != 0:
            if (len(words[i]) < 1) or (words[i-1][-1] != words[i][0]) or (words[i] in tmp):
                user_cnt = user_order
                order_cnt = len(user[user_order-1]) + 1
                return [user_cnt, order_cnt]

            else:
                user[user_order - 1].append(words[i])
        else:
            user[user_order - 1].append(words[i])
                
        
    return [user_cnt, order_cnt]
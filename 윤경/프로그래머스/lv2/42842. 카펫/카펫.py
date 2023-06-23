def solution(brown, yellow):
    answer = []
     # 전체 격자 수
    total = brown + yellow
    
    # a는 가로 길이
    for a in range(1, total+1):
        if total % a == 0:   # 나누어떨어지면
            b = total //a
            if a>=b and yellow == (a-2)*(b-2):  # brown = 2a+2b-4로 해도 됨
                answer = [a, b]
                break
    
    return answer
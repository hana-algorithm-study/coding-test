def convert(num, base):
    temp = "0123456789ABCDEF"
    q, r = divmod(num, base)

    if q == 0:
        return temp[r]
    else:
        return convert(q, base) + temp[r]
    
def solution(n, t, m, p): #n진법, 구할 숫자 개수, 인원, 순서
    answer = ''
    result = ''
    
    for i in range(m*t):
        result += str(convert(i, n))
        
    while len(answer) < t:
        answer += result[p-1]
        p += m
        
    return answer
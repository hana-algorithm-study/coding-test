def solution(n):
    bin_n = list(bin(n)[2:]).count('1')
    answer = n + 1
    while True :
        one = list(bin(answer)[2:]).count('1')
        if one == bin_n : return answer
        else : answer += 1
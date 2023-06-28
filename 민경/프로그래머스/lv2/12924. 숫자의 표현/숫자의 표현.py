def solution(n):
    answer = 1
    
    if n == 1 or n == 2 :
        return 1
    
    else :
        for i in range(1, n) :
            sum = i
            for j in range(i+1,n) :
                sum += j
                if sum == n :
                    answer += 1
                    break
                elif sum > n :
                    break

    return answer
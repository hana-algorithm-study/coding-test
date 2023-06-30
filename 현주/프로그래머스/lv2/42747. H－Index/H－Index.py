def solution(citations):
    result = 0
    citations.sort()
    for i in range(len(citations)):
        if citations[i] >= len(citations) - i:
            result +=1
    answer=result
    return answer
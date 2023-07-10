def solution(citations):
    answer = 0
    citations.sort(reverse =True)

    # 완전탐색하면서 index+1 이랑 원소값 중 작은 것 저장해서, 저장값 중 제일 큰 것 출력
    for i, x in enumerate(citations):
        tmp = min(i+1, x)
        if tmp > answer:
            answer = tmp

    return answer
# 1) 짝수인 경우 맨 끝에 1 추가
# 2) 홀수일 때는 맨 왼쪽에 0을 추가하고 맨 오른쪽 0을 찾는다.
# 2-1) 홀수: 0이 있는 경우
# 맨 오른쪽 0을 1로 바꾸고, 그 오른쪽 1을 0으로 바꾼다
# 2-2) 홀수: 모두 1인 경우
# 맨 왼쪽 1을 0으로, 그 왼쪽 0을 1로 바꾼다

def solution(numbers):
    answer = []

    for x in numbers:
        
        if x % 2 == 0:  # 짝수
            result = x+1
            answer.append(result)
            
        else:   # 홀수
            binary = '0' + bin(x)[2:]
            idx = binary.rfind('0')
            binary_list = list(binary)
            binary_list[idx:idx+2] = '10'
            result = int(''.join(binary_list), 2)
            
            answer.append(result)
        
    return answer

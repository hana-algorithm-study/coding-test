from itertools import permutations

def solution(expression):
    answer = 0
    check = []
    
    operators = ["+","-","*"]
    
    for x in list(permutations(operators, 3)):
        
        tmp = ""
        tmp_list = []
        
        # 숫자랑 부호 구분해서 list 저장
        for y in expression:            
            if y.isdigit():
                tmp += y                
            else:   # 부호일 때  
                tmp_list.append(tmp)
                tmp_list.append(y)            
                tmp = ""    # 다시 초기화
                
        tmp_list.append(tmp)    # 마지막으로 추가
        
        # 순서대로 계산
        for z in x:
            stack = []
            
            while len(tmp_list) != 0:
                tmp = tmp_list.pop(0)    
                
                if tmp == z:
                    if z == '*':                        
                        result = int(stack.pop()) * int(tmp_list.pop(0))
                    elif z == '+':
                        result = int(stack.pop()) + int(tmp_list.pop(0))
                    elif z == '-':
                        result = int(stack.pop()) - int(tmp_list.pop(0))
                    
                    result = str(result)
                    stack.append(result)
                    
                else:
                    stack.append(tmp)
            
            tmp_list = stack    # 초기화
        
        result = int(tmp_list[0])
        check.append(abs(result))   # 절대값으로 계산한 값 넣어주기
        
    answer = max(check)
        
    return answer
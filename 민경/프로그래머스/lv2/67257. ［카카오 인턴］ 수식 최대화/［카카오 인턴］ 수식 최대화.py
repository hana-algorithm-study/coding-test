from itertools import permutations

def solution(expression):
    answer = 0
    exp = []
    operator = ['*', '+','-']
    priority = list(permutations(operator))
    
    last = 0
    for i in range(len(expression)) :
        if i == len(expression) -1 :
            exp.append(expression[last:i+1])
        elif expression[i] == '-' or expression[i] == '*' or expression[i]=='+' :
            exp.append(expression[last:i])
            exp.append(expression[i])
            last = i + 1
    
    for j in range(6) :
        prior = priority[j]
        stack = []
        calculate = []
        for item in exp :
            if item.isdigit() :
                calculate.append(item)
            else :
                while stack and prior.index(item) <= prior.index(stack[-1]) :
                    calculate.append(stack.pop())
                stack.append(item)
        while stack :
            calculate.append(stack.pop())
        
        for j in calculate:
            if j.isdigit():
                stack.append(int(j))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if j == '*':
                    stack.append(num1 * num2)
                elif j == '+':
                    stack.append(num1 + num2)
                else:
                    stack.append(num1 - num2)

        result = stack.pop()
        if abs(result) > answer:
            answer = abs(result)


    return answer
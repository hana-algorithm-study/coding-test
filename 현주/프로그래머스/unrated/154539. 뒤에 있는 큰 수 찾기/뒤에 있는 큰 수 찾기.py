def solution(numbers):
    answer = []
    stack = [] #0
    answer = [-1 for i in range(len(numbers))]
    for index, val in enumerate(numbers): #0,2
        while stack and numbers[stack[-1]]<numbers[index]:
            answer[stack.pop()]=numbers[index]
        stack.append(index)
    return answer
        
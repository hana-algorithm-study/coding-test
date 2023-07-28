import math
from functools import reduce
def solution(clothes):
    answer = 0
    dict1={}
    for i in range(len(clothes)):
        if clothes[i][1] in dict1:
            dict1[clothes[i][1]]+=1
        else:
            dict1[clothes[i][1]]=1
    dict1=dict(zip(dict1.keys(),map(lambda x:x[1]+1,dict1.items()))) #입지 않을때까지 포함
    answer=reduce(lambda x, y: x * y, list(dict1.values()))-1 #전부 안입을 때 빼기
    return answer
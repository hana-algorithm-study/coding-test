import numpy as np
import math
def solution(progresses, speeds):
    answer = []
    
    pro_list=list(map(lambda x: (100- x), progresses))
    speeds=np.array(speeds)
    pro_list=np.array(pro_list)
    moc_list=pro_list/speeds
    moc_list=list(map(lambda x: math.ceil(x), moc_list))
    print(moc_list)
    
    maxDep = 0
    cnt = 1
    for i in moc_list:
        if maxDep<i:
            maxDep=i
            answer.append(cnt)
            cnt=1
        else:
            cnt+=1
    
    return answer[1:]+[cnt]
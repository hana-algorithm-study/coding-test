def solution(people, limit):
    answer = 0
    people.sort()
    two = []
    one = []
    all = len(people)
    cnt = 0
    
    s = 0
    e = len(people)-1
    
    while s <= e:
        if people[s] + people[e] <= limit and s != e:
            two.append(people[s])
            two.append(people[e])
            s += 1
            e -= 1
            cnt += 1
        else:
            one.append(people[e])
            e -= 1
            cnt += 1
    
        
    answer = cnt   
    
    return answer
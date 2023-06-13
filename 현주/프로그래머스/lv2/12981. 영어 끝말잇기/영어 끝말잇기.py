def solution(n, words):
    w = [words[0][0]] #첫글자
    
    for i, v in enumerate(words): #index, 값
        if v not in w and w[-1][-1] == v[0]: #앞자리만
            w.append(v)
        else:
            return [i % n + 1, (i//n)+1]
    return [0, 0]
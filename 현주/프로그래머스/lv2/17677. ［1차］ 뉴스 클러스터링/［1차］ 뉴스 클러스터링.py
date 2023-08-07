from collections import Counter
def solution(str1, str2):
    str1=str1.lower()
    str2=str2.lower()
    list1=[]
    list2=[]
    for i in range(len(str1)-1):
        if(str1[i:i+2].isalpha()):
            list1.append(str1[i:i+2])
    for j in range(len(str2)-1):
        if str2[j:j+2].isalpha():
            list2.append(str2[j:j+2])

    if not list1 and not list2:
        return 65536
    c1 = Counter(list1)
    c2 = Counter(list2)
    answer = int(float(sum((c1&c2).values()))/float(sum((c1|c2).values())) * 65536)
    return answer
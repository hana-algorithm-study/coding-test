arr = []
m=int(input())
for _ in range(m): # m번 loop을 돌면서 input을 arr에 append
	arr.append(input())

for i in arr:
    cnt=0
    def recursion(s, l, r):
        global cnt
        cnt+=1
        if l >= r: return 1
        elif s[l] != s[r]: return 0
        else: return recursion(s, l+1, r-1)

    def isPalindrome(s): 
        return recursion(s, 0, len(s)-1)

    
    print(isPalindrome(i), cnt)
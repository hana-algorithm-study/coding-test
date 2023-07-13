def solution(n, computers):


    def dfs(v):
        visited[v]=True
        
        for neighbor in range(n): #2차원 배열
            if not visited[neighbor] and computers[v][neighbor]:
                dfs(neighbor)
    count=0
    visited=[False]*n
    
    for idx in range(n):
        if not visited[idx]:
            dfs(idx)
            count+=1
    return count
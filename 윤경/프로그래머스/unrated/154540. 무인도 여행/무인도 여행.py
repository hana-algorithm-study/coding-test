import sys
sys.setrecursionlimit(10**5)

def dfs(maps, x, y, visit):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    visit[x][y] = 1 # 방문한 것으로 바꾸기
    result = int(maps[x][y])
    
    for l in range(4):            
        if 0 <= x+dx[l] < len(maps) and 0 <= y+dy[l] < len(maps[0]):
            now = maps[x+dx[l]][y+dy[l]]
            
            if now != 'X' and visit[x+dx[l]][y+dy[l]] == 0: # 아직 방문 안 함
                result += dfs(maps, x+dx[l], y+dy[l], visit)
            
    return result

def solution(maps):
    answer = []
    visit = [[0] * len(maps[0]) for _ in range(len(maps))]
    result = 0
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and visit[i][j] == 0:
                result = dfs(maps, i, j, visit)
                answer.append(result)
    
    if len(answer) > 0:
        answer = sorted(answer)
        return answer
    else:
        return [-1]
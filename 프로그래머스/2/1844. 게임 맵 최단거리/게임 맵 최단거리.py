from collections import deque

def solution(maps):
    maps_r = len(maps)
    maps_c = len(maps[0])
    
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    def bfs(r, c):
        queue = deque()
        queue.append((r, c))
        
        while queue:
            r, c = queue.popleft()
            
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                
                if nr < 0 or nr >= maps_r or nc < 0 or nc >= maps_c:
                    continue
                
                if maps[nr][nc] == 0:
                    continue
                
                if maps[nr][nc] == 1:
                    maps[nr][nc] = maps[r][c] + 1
                    queue.append((nr, nc))
        
        if maps[maps_r-1][maps_c-1] > 1:
            return maps[maps_r-1][maps_c-1]
        else:
            return -1
        
    return bfs(0, 0)
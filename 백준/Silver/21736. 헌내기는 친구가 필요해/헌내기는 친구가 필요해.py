import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())

campus = []
start_r, start_c = 0, 0

for i in range(N):
    row = list(sys.stdin.readline().strip())
    campus.append(row)

    # 다연이의 위치 파악
    if 'I' in row:
        start_r = i
        start_c = row.index('I')

visited = [[False] * M for _ in range(N)]
count = 0

def dfs(r, c):
    global count 
    visited[r][c] = True

    if campus[r][c] == 'P':
        count += 1

    # 0~3 인덱스가 각 순서대로 상,하,좌,우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(4):
        now_r = r + dr[i]
        now_c = c + dc[i]

        if 0 <= now_r < N and 0 <= now_c < M: # 맵 범위 내에 존재
            if not visited[now_r][now_c] and campus[now_r][now_c] != 'X': # 방문하지 않았고, 벽이 아닌 경우
                dfs(now_r, now_c)

dfs(start_r, start_c)

if count == 0:
    print("TT")
else:
    print(count)

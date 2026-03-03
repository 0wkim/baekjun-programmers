import sys
from collections import deque
sys.setrecursionlimit(10**6)

# NxM 크기의 미로
N, M = map(int, sys.stdin.readline().split())

# DFS (깊이 우선 탐색)
# 한 방향으로 최대한 깊이 가다가, 
# 더이상 갈 곳이 없으면 가장 마지막에 만난 갈림길로 돌아가 다른 방향 탐색 
# 구현: 재귀 함수, 스택
# visited로 방문 처리 

# BFS (너비 우선 탐색)
# 시작 정점으로부터 가까운 정점을 먼저 방문하고, 멀리 떨어진 것을 나중에 방문
# 구현: 큐(collections.deque)
# 큐에서 노드를 하나씩 꺼내며 연결된 노드 중 방문하지 않은 곳을 큐에 넣어 방문 처리

graph = []
for _ in range(N):
    line = list(map(int, sys.stdin.readline().strip()))
    graph.append(line)

visited_bfs = [[False] * M for _ in range(N)]

def bfs(r, c):
    queue = deque([(r, c)])
    visited_bfs[r][c] = True

    # 상하 좌우 
    move_r = [-1, 1, 0, 0]
    move_c = [0, 0, -1, 1]

    while queue:
        # 이전 칸
        curr_r, curr_c = queue.popleft()

        for i in range(4):
            nr = curr_r + move_r[i]
            nc = curr_c + move_c[i]

            # 미로 범위 내에 있고, 길(1)이며, 아직 방문하지 않았다면 
            if 0 <= nr < N and 0 <= nc < M:
                if graph[nr][nc] == 1 and not visited_bfs[nr][nc]:
                    visited_bfs[nr][nc] = True 

                    # 이전 칸의 거리 + 1을 현재 칸에 저장 
                    # 칸을 이동할 때마다 최소 거리를 저장하는 것 
                    graph[nr][nc] = graph[curr_r][curr_c] + 1
                    queue.append((nr, nc))

bfs(0, 0)
print(graph[N-1][M-1])
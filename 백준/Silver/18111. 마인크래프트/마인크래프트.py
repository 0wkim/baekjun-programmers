import sys
from collections import Counter

N, M, B = map(int, sys.stdin.readline().split())

field = []
for _ in range(N):
    # 한 줄(M개)의 높이 정보를 리스트로 받아 추가
    field.extend(map(int, sys.stdin.readline().split()))

# 각 높이의 빈도수 계산
# ex) 0: 11 -> 높이 0인 땅이 11개 존재
height_counts = Counter(field)

ans_time = float('inf')
ans_height = 0 # 최소 시간일 때의 높이 

# 모든 높이일 경우를 시도하여 시간이 가장 적게 걸리는 것을 탐색
for target in range(257):
    removed = 0 # 깎아서 얻은 블록 (2초 소요)
    added = 0 # 쌓아서 쓴 블록 (1초 소요)

    # field 전체를 순회하지 않고, 존재하는 높이만 순회  
    for height, count in height_counts.items():
        # 땅의 높이가 target보다 높은 경우 깎아서 제거
        if height > target:
            removed += (height - target) * count
        else:
            # 땅의 높이가 target보다 낮은 경우 쌓아서 추가
            added += (target - height) * count 
    
    # 인벤토리 블록의 개수 확인 
    # (처음 가진 블록 B + 깎아서 얻은 블록 added)가 (쌓는데 사용한 블록 removed)보다 많아야 함
    if removed + B >= added:
        time = removed * 2 + added
        
        # 최소 시간 갱신
        if time <= ans_time:
            ans_time = time
            ans_height = target
    
print(ans_time, ans_height)

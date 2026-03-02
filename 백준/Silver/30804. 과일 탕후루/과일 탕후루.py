import sys

N = int(sys.stdin.readline())

fruits = list(map(int, sys.stdin.readline().split()))

# 과일 종류별 개수
# ex) count[3] = 2 -> 3번 과일이 두개 존재하는 것 
count = [0]*10 # 0번 인덱스는 사용하지 않음

left = 0
now_types = 0 # 현재까지 보유한 과일 종류의 수 
max_cnt = 0 # 최대 과일 개수 

for right in range(N):
    # 과일 추가
    if count[fruits[right]] == 0:
        now_types += 1
    count[fruits[right]] += 1

    # 과일 종류가 2개를 초과하면 left 이동
    # 과일 종류를 줄이기 위해 가장 예전에 넣었던 왼쪽 끝(left) 과일부터 제거 
    while now_types > 2:
        count[fruits[left]] -= 1
        if count[fruits[left]] == 0: # 과일 개수가 0이면 해당 과일 종류 제거
            now_types -= 1
        left += 1

    # 최대 과일 개수 갱신
    now_cnt = right - left + 1
    if now_cnt > max_cnt:
        max_cnt = now_cnt

print(max_cnt)

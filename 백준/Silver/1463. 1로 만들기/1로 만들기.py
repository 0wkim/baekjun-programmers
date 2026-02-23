import sys

N = int(sys.stdin.readline())

counts = [0] * (N + 1)

def solution(N):
    for i in range(2, N + 1):
        # 1을 빼는 경우 (비교하기 위한 기본값으로 설정)
        counts[i] = counts[i-1] + 1   # (전 단계 횟수 + 1)

        # 2로 나누는 경우
        if i % 2 == 0:
            counts[i] = min(counts[i], counts[i//2] + 1)

        # 3으로 나누는 경우 
        if i % 3 == 0:
            counts[i] = min(counts[i], counts[i//3] + 1)

    return counts[N]

print(solution(N))
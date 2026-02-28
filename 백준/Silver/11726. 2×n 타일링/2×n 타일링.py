import sys

N = int(sys.stdin.readline())

# dp[i] = 가로 길이가 i일 때, 타일을 채울 수 있는 모든 경우의 수 
dp = [0] * (N+1)

dp[1] = 1

# 런타임 에러 방지
if N >= 2:
    dp[2] = 2

for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[N])
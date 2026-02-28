import sys

# 누적 합 개념
# 예를들어 1~50까지의 숫자가 있을때, 30~50의 합을 구하려면 1~50의 합에서 1~29의 합을 빼면 되는 것
# 즉, i~j의 합은 0~j의 합에서 0~i-1의 합을 뺀 것 

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

# 누적 합
prefix_sum = [0] *( N+1)
for i in range(N):
    prefix_sum[i+1] = prefix_sum[i] + numbers[i]

def solution(i, j):
    sum_num = prefix_sum[j] - prefix_sum[i-1]
    print(sum_num)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    solution(i, j)



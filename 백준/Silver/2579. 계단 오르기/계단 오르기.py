import sys

N = int(sys.stdin.readline())

stairs = []
stairs.append(0)
for _ in range(N):
    stairs.append(int(sys.stdin.readline()))

score = [0]*301
score[1] = stairs[1]
if N >= 2:
    score[2] = stairs[1] + stairs[2]
if N >= 3:
    score[3] = max(stairs[1]+stairs[3], stairs[2]+stairs[3])

for i in range(4, N+1):
    score[i] = max(score[i-3]+stairs[i-1]+stairs[i], score[i-2]+stairs[i])

print(score[N])
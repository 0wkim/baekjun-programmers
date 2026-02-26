import sys

# INPUT = list(map(int, sys.stdin.readline().split()))

N, M = map(int, sys.stdin.readline().split())

no_hear = set()
no_see = set()

for _ in range(N):
    no_hear.add(sys.stdin.readline().strip())

for _ in range(M):
    no_see.add(sys.stdin.readline().strip())

# 교집합 연산 사용
no_hear_see = list(no_hear & no_see)
no_hear_see.sort()

print(len(no_hear_see))
for name in no_hear_see:
    print(name)
import sys

T = int(sys.stdin.readline())

zero = [1, 0, 1]
one = [0, 1, 1]

def solution(N):
    length = len(zero)
    if N >= length:
        for i in range(length, N+1): 
            zero.append(zero[i-2] + zero[i-1])
            one.append(one[i-2] + one[i-1])
    print(f"{zero[N]} {one[N]}")

for _ in range(T):
    N = int(sys.stdin.readline())
    solution(N)
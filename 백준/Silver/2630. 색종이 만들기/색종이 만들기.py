import sys
from collections import Counter

N = int(sys.stdin.readline())

paper = []

for _ in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))

blue = 0
white = 0

def solution(x, y, size):
    global blue, white
    color = paper[x][y] # 0은 흰색, 1은 파란색

    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color: # 컬러가 하나라도 다를 경우
                new_size = size // 2

                solution(x, y, new_size) # 1사분면
                solution(x + new_size, y, new_size) # 2사분면
                solution(x, y + new_size, new_size) # 3사분면
                solution(x + new_size, y + new_size, new_size) # 4사분면
                
                return

    # 반복문을 통과했으면 모두 같은 색상이라는 것
    if color == 0:
        white += 1
    else:
        blue += 1

solution(0, 0, N)

print(white)
print(blue)

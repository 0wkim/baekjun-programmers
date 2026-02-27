import sys

# INPUT = list(map(int, sys.stdin.readline().split()))

# key: 주소, value: 비밀번호 

T = int(sys.stdin.readline())

def solution(N):
    category_list = []
    closet = {}

    for _ in range(N):
        _, category = sys.stdin.readline().split()
        category_list.append(category)

        if category in closet.keys():
            closet[category] += 1
        else:
            closet[category] = 1
    
    result = 1

    for key in closet.keys():
        closet[key] += 1
    
    for value in closet.values():
        result *= value
    
    print(result-1)

for _ in range(T):
    N = int(sys.stdin.readline())
    solution(N)


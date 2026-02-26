import sys

# INPUT = list(map(int, sys.stdin.readline().split()))

S = set()
M = int(sys.stdin.readline())

for _ in range(M):
    calc = sys.stdin.readline().split()
    command = calc[0]

    if command == "all":
        S = set([i for i in range(1, 21)])
    elif command == "empty":
        S = set()

    else:
        number = int(calc[1])
        
        if command == "add":
            S.add(number)
        elif command == "remove":
            S.discard(number)
        elif command == "check":
            if number in S:
                print(1)
            else:
                print(0)
        elif command == "toggle":
            if number in S:
                S.discard(number)
            else:
                S.add(number)
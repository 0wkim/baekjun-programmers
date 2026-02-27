import sys

# INPUT = list(map(int, sys.stdin.readline().split()))

# 그리디 알고리즘 
# 인출 시간이 짧은 사람을 앞쪽에 세울 것 

N = int(sys.stdin.readline())

atm_list = list(map(int, sys.stdin.readline().split()))
atm_list.sort()

times = []

for i in range(len(atm_list)):
    total_time = sum(atm_list[0:i+1])
    times.append(total_time)

print(sum(times))


    
import sys
'''
k+1로 나눈 몫을 먼저 더하고 나머지 값만큼 더하여 구해도 될듯
'''

n, m, k = map(int, sys.stdin.readline().split())

data = list(map(int, sys.stdin.readline().split()))

data = sorted(data)
tmp = k
result = 0

while m > 0:
    result += data[-1]
    m -= 1
    tmp -= 1

    if tmp == 0:
        tmp = k
        m -= 1
        result += data[-2]

print(result)

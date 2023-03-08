import sys

n, m = map(int, sys.stdin.readline().split())

result = []

for i in range(n):
    min_value = min(list(map(int, sys.stdin.readline().split())))
    result.append(min_value)

print(max(result))
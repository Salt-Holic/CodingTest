import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
add = [arr[0]]

for i in range(n-1):
    add.append(max(add[i] + arr[i+1], arr[i+1]))

print(max(add))

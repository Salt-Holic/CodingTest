from math import gcd
n = int(input())

arr = []
interval = []
m = []

for i in range(n):
    arr.append(int(input()))

for i in range(n - 1):
    interval.append(arr[i + 1] - arr[i])

prev = interval[0]

for i in range(1, len(interval)):
    prev = gcd(prev, interval[i])

for i in range(2, int(prev ** 0.5) + 1):
    if prev % i == 0:
        m.append(i)
        m.append(prev // i)
m.append(prev)
m = list(set(m))
m.sort()
print(*m)

'''
A = a*m +r
B = b*m +r
C = c*m +r

B-A = (b-a)m
C-B = (c-b)m

c-b != b-a
즉, c-b, b-a의 공약수를 구하면 m값을 알 수 있음
m의 제곱근도 m의 포함됨

18 % 2 = 0 ( 2 = 약수)
18 // 2 = 9 ( 9 = 약수)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
'''

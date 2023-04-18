n = int(input())
rings = list(map(int, input().split()))


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


for i in range(1, len(rings)):
    div = gcd(rings[0], rings[i])
    print(str(rings[0]//div) + '/' + str(rings[i]//div))

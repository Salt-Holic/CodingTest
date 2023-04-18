t = int(input())

for j in range(t):
    n = int(input())
    cloths ={}
    for i in range(n):
        _, wear = input().split()
        if wear not in cloths:
            cloths[wear] = 2
        else:
            cloths[wear] += 1

    result = 1
    for _, i in cloths.items():
        result *= i

    print(result-1)
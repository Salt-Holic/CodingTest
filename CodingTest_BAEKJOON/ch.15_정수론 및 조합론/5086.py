n, m = -1, -1

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    if n > m:
        if n % m == 0:
            print('multiple')
            continue
        print('neither')
    else:
        if m % n == 0:
            print('factor')
            continue
        print('neither')

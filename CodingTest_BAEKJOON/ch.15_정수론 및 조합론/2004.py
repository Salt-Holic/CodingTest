n, m = map(int, input().split())


def counter(n, t):
    cnt = 0
    while n >= t:
        cnt += n // t
        n //= t
    return cnt


cnt_5 = counter(n, 5) - counter(m, 5) - counter(n - m, 5)
cnt_2 = counter(n, 2) - counter(m, 2) - counter(n - m, 2)
print(min(cnt_2, cnt_5))

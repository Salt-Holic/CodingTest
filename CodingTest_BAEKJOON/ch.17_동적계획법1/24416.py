n = int(input())
cnt1, cnt2 = 0, 0
fib_data = [0 for i in range(n + 1)]
fib_data[0], fib_data[1], fib_data[2] = 0, 1, 1


def fib_rec(n):
    global cnt1
    cnt1 += 1
    if n == 1 or n == 2:
        cnt1 -= 1
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)


def fib_dp(n):
    global cnt2

    for i in range(3, n + 1):
        fib_data[i] = fib_data[i - 1], fib_data[i - 2]
        cnt2 += 1


# 단순 계산만으로 반복횟수를 알아낼 수 있음
def fib(n):
    a, b = 1, 1

    for i in range(n - 2):
        a, b = b, a + b

    return b


def fibonacci(n):
    return n - 2


fib_rec(n)
fib_dp(n)
print(cnt1 + 1, cnt2, fib(n), fibonacci(n))

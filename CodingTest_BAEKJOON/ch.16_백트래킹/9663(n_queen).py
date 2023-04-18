n = int(input())

cnt = 0
col = [0] * n


def is_promising(x):
    for i in range(x):
        if col[x] == col[i] or abs(col[x] - col[i]) == abs(x - i):
            return False

    return True


def n_queen(x):
    global cnt
    if x == n:
        cnt += 1
        return

    else:
        for i in range(n):
            col[x] = i
            if is_promising(x):
                n_queen(x + 1)


n_queen(0)
print(cnt)

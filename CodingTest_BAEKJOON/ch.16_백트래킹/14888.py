n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
result = []


def calculate(idx, num):
    global add, sub, mul, div
    if idx == n:
        result.append(num)
        return
    else:
        if add > 0:
            add -= 1
            calculate(idx+1, num+nums[idx])
            add += 1
        if sub > 0:
            sub -= 1
            calculate(idx+1, num-nums[idx])
            sub += 1
        if mul > 0:
            mul -= 1
            calculate(idx+1, num*nums[idx])
            mul += 1
        if div > 0:
            div -= 1
            calculate(idx+1, int(num/nums[idx]))  # -n 도 고려할것
            div += 1


calculate(1, nums[0])

print(max(result))
print(min(result))
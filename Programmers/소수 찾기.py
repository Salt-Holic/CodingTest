def isPrime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def makeNum(nums, prime, temp):
    l = list(nums)

    for i in nums:
        temp += i
        prime.append(int(temp))
        l.remove(i)
        makeNum(l, prime, temp)
        l.append(i)
        temp = temp[:-1]


def solution(numbers):
    prime = []

    makeNum(numbers, prime, '')
    prime = list(filter(isPrime, set(prime)))

    return len(prime)
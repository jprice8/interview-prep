def fibMemo(n, memo = {}):
    if n in memo: return memo[n]
    if n <= 2: return 1
    memo[n] = fibMemo(n - 1, memo) + fibMemo(n - 2, memo)
    return memo[n]


def fibTab(n):
    table = [0 for _ in range(n + 1)]
    table[1] = 1

    # for i in range(n - 1):
    i = 0
    while i <= n:
        table[i + 1] += table[i]
        table[i + 2] += table[i]

        i += 1

def aeSolution(n):
    lastTwo = [0, 1]
    counter = 3

    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]


if __name__ == '__main__':
    # print(fibMemo(6))

    print(aeSolution(6)) # 8
    # print(fibTab(7)) # 13 
    # print(fibTab(8)) # 21
    # print(fibTab(50)) # 12586269025
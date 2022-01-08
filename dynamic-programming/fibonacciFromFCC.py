def fibMemo(n, memo = {}):
    if n in memo: return memo[n]
    if n <= 2: return 1
    memo[n] = fibMemo(n - 1, memo) + fibMemo(n - 2, memo)
    return memo[n]

if __name__ == '__main__':
    n = 4
    print(fibMemo(n))
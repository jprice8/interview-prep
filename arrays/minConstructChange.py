

def minConstructChange(coins):
    sum = 0

    coins = sorted(coins)

    if len(coins) == 0:
        return 1

    for coin in coins:
        if coin > sum + 1:
            return sum + 1
        else:
            sum += coin

    return sum + 1


coins = [1, 1, 1, 1, 1]
print(minConstructChange(coins))
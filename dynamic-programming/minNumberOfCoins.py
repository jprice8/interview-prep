

def minNumberOfWaysForChange(n, denoms):
    result = [0 for idx in range(n + 1)]
    result[0] = 1
    remaining = n

    # Count min ways to create change for 1 through n + 1
    for i in range(1, n + 1):
        # Check denoms in reverse order
        for j in reversed(range(len(denoms))):
            denom = denoms[j]
            # If denom is L.T.E. current index, it will make change
            if denom <= i:
                changeProduced = handleMakeChange(i, denom, result)
                if changeProduced == i:
                    break

    return checkForCorrectChange(remaining, result)


def handleMakeChange(i, denom, result):
    floor = i // denom 
    result[i] += floor 
    return floor * denom


def checkForCorrectChange(remaining, result):
    # If none remaining we have correct change
    if remaining == 0:
        return result[-1]
    # Else we don't and return -1
    else:
        return -1
    

if __name__ == '__main__':
    n = 7
    denoms = [1, 5, 10]
    print(minNumberOfWaysForChange(n, denoms))
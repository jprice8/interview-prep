def ambiguousMeasurements(measuringCups, low, high):
    # Base case
    if low <= 0 or high <= 0:
        return False 

    # Recursive call
    for cup in measuringCups:
        lowCupLevel = cup[0]
        highCupLevel = cup[1]

        if highCupLevel <= high and low <= lowCupLevel:
            return True 

        return ambiguousMeasurements(measuringCups, low - lowCupLevel, high - highCupLevel)


# O(low * high * n) time - where n is the number of cups.
# Time complexity is due to us not knowing how many or what size cups we will have.
# E.g. If we have low of 2100 and one cup of size 1, we will have to recursively call 2100 times.
# Same for high.
# For every recursive call, we loop through n cups.
#
# O(low * high) space - Due to our memo hash table which will have, at worst, low * high space.
def aeSolution(measuringCups, low, high):
    memoization = {}
    return canMeasureInRange(measuringCups, low, high, memoization)


def canMeasureInRange(measuringCups, low, high, memoization):
    memoizeKey = createHashableKey(low, high)
    if memoizeKey in memoization:
        return memoization[memoizeKey]

    if low <= 0 and high <= 0:
        return False 

    canMeasure = False 
    for cup in measuringCups:
        lowCupLevel, highCupLevel = cup

        if low <= lowCupLevel and highCupLevel <= high:
            canMeasure = True 
            break 

        newLow = max(0, low - lowCupLevel)
        newHigh = max(0, high - highCupLevel)
        canMeasure = canMeasureInRange(measuringCups, newLow, newHigh, memoization)
        if canMeasure:
            break

    memoization[memoizeKey] = canMeasure
    return canMeasure

def createHashableKey(low, high):
    return str(low) + str(high)


if __name__ == '__main__':
    # measuringCups = [
    #     [200, 210],
    #     [450, 465],
    #     [800, 850]
    # ]
    # print(aeSolution(measuringCups, 2100, 2300))

    measuringCups = [
        [50, 50]
    ]
    print(aeSolution(measuringCups, 200, 200))
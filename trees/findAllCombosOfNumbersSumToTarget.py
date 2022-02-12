from typing import List


def shoppingOptions(a: List[int], b: List[int], c: List[int], d: List[int], limit: int) -> int:
    all_numbers = [a, b, c, d] 
    n = len(all_numbers)
    for numbers in all_numbers:
        numbers.sort()

    # Cost of (lowest, highest) combo
    ranges = [(0, 0)]
    # Number of all combos, ignoring limit
    combinations = [1]
    for numbers in all_numbers:
        low, high = ranges[-1]
        ranges.append((numbers[0] + low, numbers[-1] + high))
        combinations.append(len(numbers) * combinations[-1])


def shoppingOptions(pairOfJeans, pairOfShoes, pairOfSkirts, pairOfTops, budget):
    hashMap = {}
    count = 0

    for jean in pairOfJeans:
        for shoe in pairOfShoes:
            costSum = jean + shoe
            if costSum in hashMap:
                hashMap[costSum] += 1
            else:
                hashMap[costSum] = 1

    for skirt in pairOfSkirts:
        for top in pairOfTops:
            remainingBudget = budget - (skirt + top)
            hashKeys = [jeanShoeSum for jeanShoeSum in hashMap if jeanShoeSum <= remainingBudget]
            hashValues = [hashMap.get(k) for k in hashKeys]

            count += sum(hashValues)

    return count



if __name__ == '__main__':
    pairOfJeans = [2]
    pairOfShoes = [3, 4]
    pairOfSkirts = [2, 5]
    pairOfTops = [4, 6]

    print(shoppingOptions(pairOfJeans, pairOfShoes, pairOfSkirts, pairOfTops, 12)) # 2
    
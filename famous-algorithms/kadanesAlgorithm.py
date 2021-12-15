# Algorithm to return maximum subarray in array

from typing import List


def kadanesAlgorithm(array: List[int]) -> List[int]:
    """
    Take in array and return maximum subarray.
    """
    maxEndingHere = array[0]
    maxSoFar = array[0]
    for i in range(1, len(array)):
        num = array[i]
        maxEndingHere = max(num, maxEndingHere + num)
        maxSoFar = max(maxSoFar, maxEndingHere)

    return maxEndingHere


print(kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))
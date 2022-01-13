# O(b^2r) time | O(b) space - where b is the number of hashmaps in blocks and r is length of reqs.
def apartmentHunting(blocks, reqs):
    maxDistancesAtBlocks = [float("-inf") for _ in blocks]

    for i in range(len(blocks)):
        for req in reqs:
            closestReqDistance = float("inf")
            for j in range(len(blocks)):
                if blocks[j][req]:
                    closestReqDistance = min(closestReqDistance, getDistance(i, j))
            maxDistancesAtBlocks[i] = max(maxDistancesAtBlocks[i], closestReqDistance)

    return getIdxAtMinValue(maxDistancesAtBlocks)


def getIdxAtMinValue(array):
    idxAtLowestValue = 0
    for idx, _ in enumerate(array):
        if array[idx] < array[idxAtLowestValue]:
            idxAtLowestValue = idx
    return idxAtLowestValue


def getDistance(a, b):
    return abs(a - b)


if __name__ == '__main__':
    blocks = [
        {
            "gym": False,
            "school": True,
            "store": False,
        },
        {
            "gym": True,
            "school": False,
            "store": False,
        },
        {
            "gym": True,
            "school": True,
            "store": False,
        },
        {
            "gym": False,
            "school": True,
            "store": False,
        },
        {
            "gym": False,
            "school": True,
            "store": True,
        },
    ]
    reqs = ["gym", "school", "store"]
    print(apartmentHunting(blocks, reqs))
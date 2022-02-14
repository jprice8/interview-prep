# O(n * b) time - where n is the length of boxTypes and b is the number of boxes for each boxType.
# O(1) space
# def fillTruck(boxTypes, truckSize):
#     boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True) 
#     totalBoxes = 0
#     totalUnits = 0

#     for box in boxTypes:
#         while totalBoxes < truckSize and box[0] > 0:
#             totalBoxes += 1
#             totalUnits += box[1]
#             box[0] -= 1

#     return totalUnits

# O(nlog(n)) time 
# O(1) space
def fillTruck(boxTypes, truckSize):
    boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
    totalUnits = 0
    i = 0
    while i < len(boxTypes) and truckSize > 0:
        totalUnits += min(truckSize, boxTypes[i][0]) * boxTypes[i][1]

        truckSize -= boxTypes[i][0]
        i += 1

    return totalUnits


if __name__ == '__main__':
    boxTypes = [
        [5, 10],
        [2, 5],
        [4, 7],
        [3, 9],
    ]
    truckSize = 10
    print(fillTruck(boxTypes, truckSize))
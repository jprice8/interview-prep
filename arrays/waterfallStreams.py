# O(w^2 * h) time | O(w) space - where w and h are the width and height of
# the array.
def waterfallStreams(array, source):
    rowAbove = array[0][:]
    # Set initial water source
    rowAbove[source] = -1

    for row in range(1, len(array)):
        currentRow = array[row][:]

        # Loop through each cell in row
        for idx in range(len(rowAbove)):
            valueAbove = rowAbove[idx]

            # Two bools, 
            # one if we have water above, 
            hasWaterAbove = valueAbove < 0
            # other if we are a block.
            hasBlock = currentRow[idx] == 1

            if not hasWaterAbove:
                continue

            if not hasBlock:
                # If there is no block in the current column, move the water down.
                currentRow[idx] += valueAbove
                continue 

            # If water above and block...
            splitWater = valueAbove / 2
            
            # Move water right.
            rightIdx = idx
            while rightIdx + 1 < len(rowAbove):
                rightIdx += 1
                if rowAbove[rightIdx] == 1: # If there is a block in the way
                    break 
                if currentRow[rightIdx] != 1: # If there is no block below us
                    currentRow[rightIdx] += splitWater
                    break 

            # Move water left.
            leftIdx = idx 
            while leftIdx - 1 >= 0:
                leftIdx -= 1
                if rowAbove[leftIdx] == 1:
                    break 
                if currentRow[leftIdx] != 1:
                    currentRow[leftIdx] += splitWater
                    break 
        rowAbove = currentRow

    finalPercentages = list(map(lambda num: num * -100, rowAbove))
    return finalPercentages


if __name__ == '__main__':
    array = [
        [0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0],
    ]
    source = 3
    print(waterfallStreams(array, source))
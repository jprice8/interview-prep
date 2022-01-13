def zigzagTaversal(array):
    height = len(array) - 1
    width = len(array[0]) - 1
    result = []
    row, col = 0, 0
    goDown = True

    while not isOutOfBounds(row, col, height, width):
        result.append(array[row][col])
        # Go down
        if goDown:
            if col == 0 or row == height:
                goDown = False 
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
            
        # Go up
        else:
            if row == 0 or col == width:
                goDown = True
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1

    return result


def isOutOfBounds(row, col, height, width):
    return row < 0 or row > height or col < 0 or col > width


if __name__ == '__main__':
    array = [
        [1, 3, 4, 10],
        [2, 5, 9, 11],
        [6, 8, 12, 15],
        [7, 13, 14, 16],
    ]
    print(zigzagTaversal(array))
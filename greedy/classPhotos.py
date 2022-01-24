# O(n) time | O(1) space - where n is the length of both arrays.
def classPhotos(redShirtHeights, blueShirtHeights):
    # tallerColorCount = {"RED": 0, "BLUE": 0} 

    # i = 0
    # while i < len(redShirtHeights):
    #     redHeight = redShirtHeights[i]
    #     blueHeight = blueShirtHeights[i]

    #     # Compare heights, taller color gets a point
    #     if redHeight > blueHeight:
    #         tallerColorCount["RED"] += 1
    #     else:
    #         tallerColorCount["BLUE"] += 1

    #     i += 1

    # # Check that at least map value is 0
    # if tallerColorCount["RED"] > 0 and tallerColorCount["BLUE"] > 0:
    #     return False
    # else:
    #     return True

    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    shirtColorInFirstRow = "RED" if redShirtHeights[0] < blueShirtHeights[0] else "BLUE"
    for i in range(len(redShirtHeights)):
        redHeight = redShirtHeights[i]
        blueHeight = blueShirtHeights[i]

        if shirtColorInFirstRow == "RED":
            if redHeight > blueHeight:
                return False 
        else:
            if blueHeight > redHeight:
                return False

    return True



if __name__ == '__main__':
    redShirtHeights = [5, 8, 1, 3, 4]
    blueShirtHeights = [6, 9, 2, 4, 5]
    print(classPhotos(redShirtHeights, blueShirtHeights)) # True

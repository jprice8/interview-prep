# def isWinner(codeList, shoppingCart):
#     # Sliding window
#     codeIndex = 0
#     # Iterate through each sublist in codelist
#     while codeIndex < len(codeList):
#         subList = codeList[codeIndex]
#         result = checkForSublist(subList, shoppingCart)

#         # If sublist is not in big list
        
#         codeIndex += 1
    
    
# def checkForSublist(subList, bigList):
#     """
#     Sliding window helper method to see if a sublist is in
#     a bigger list.
#     """
#     pass

# Return 1 or 0 for winner or loser.
# def isWinner(codeList, shoppingCart):
#     cartIdx, codeIdx = 0, 0

#     while cartIdx < len(shoppingCart) and codeIdx < len(codeList):
#         currentShoppingItem = shoppingCart[cartIdx]
#         currentCodeList = codeList[codeIdx]
#         # If the first fruit of the codeList is anything or if it matches the current fruit at the cart idx.
#         if currentCodeList[0] == 'anything' or currentCodeList[0] == currentShoppingItem and hasOrder(shoppingCart, cartIdx, currentCodeList):
#             cartIdx += len(codeList[codeIdx])
#             codeIdx += 1
#         else:
#             cartIdx += 1

#     return 1 if codeIdx == len(codeList) else 0


# def hasOrder(shoppingCart, cartIdx, currentCodeLIst):
#     for code in currentCodeLIst:
#         if cartIdx < len(shoppingCart) and code == 'anything' or shoppingCart[cartIdx] == code:
#             cartIdx += 1
#         else:
#             return False 

#     return True


def isWinner(codeList, shoppingCart):
    # Handle edge case of no code list
    if len(codeList) == 0:
        return 1

    codeIdx = 0
    cartIdx = 0

    while codeIdx < len(codeList) and cartIdx < len(shoppingCart):
        currentCodeList = codeList[codeIdx]
        currentShoppingItem = shoppingCart[cartIdx]

        if currentCodeList[0] == 'anything' or currentCodeList[0] == currentShoppingItem:
            # Potential match
            if checkForMatch(currentCodeList, cartIdx, shoppingCart):
                cartIdx += len(currentCodeList)
                codeIdx += 1
        else:
            cartIdx += 1

    return 1 if codeIdx == len(codeList) else 0


def checkForMatch(currentCodeList, cartIdx, shoppingCart):
    # Check to see we have enough room to index shopping cart
    # if len(currentCodeList) + cartIdx > len(shoppingCart) - 1:
        # return False

    # Loop through code list
    tmpCartIdx = cartIdx
    for codeItem in currentCodeList:
        if codeItem == shoppingCart[tmpCartIdx] or codeItem == 'anything':
            tmpCartIdx += 1
        else:
            return False 

    return True


if __name__ == '__main__':
    codeList = [
        ['apple', 'apple'],
        ['banana', 'anything', 'banana']
    ]

    # shoppingCart = ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']
    shoppingCart1 = ['apple', 'banana', 'orange', 'banana']

    print(isWinner(codeList, shoppingCart1))
def isWinner(codeList, shoppingCart):
    # Sliding window
    codeIndex = 0
    # Iterate through each sublist in codelist
    while codeIndex < len(codeList):
        subList = codeList[codeIndex]
        result = checkForSublist(subList, shoppingCart)

        # If sublist is not in big list
        
        codeIndex += 1
    
    
def checkForSublist(subList, bigList):
    """
    Sliding window helper method to see if a sublist is in
    a bigger list.
    """
    pass


if __name__ == '__main__':
    codeList = [
        ['apple', 'apple'],
        ['banana', 'anything', 'banana']
    ]

    shoppingCart = ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']

    print(isWinner(codeList, shoppingCart))
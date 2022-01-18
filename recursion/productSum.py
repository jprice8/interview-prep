def productSum(array, multiplier=1):
    pSum = 0
    
    for element in array:
        if type(element) is list: 
            pSum += productSum(element, multiplier + 1)
        else:
            pSum += element

    return pSum * multiplier


if __name__ == '__main__':
    array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
    print(productSum(array))
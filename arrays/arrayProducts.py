def arrayProducts(array):
    products = [1 for _ in range(len(array))]
    leftProducts = [1 for _ in range(len(array))]
    rightProducts = [1 for _ in range(len(array))]

    leftRunningProduct = 1
    for i in range(len(array)):
        leftProducts[i] = leftRunningProduct
        leftRunningProduct *= array[i]

    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        rightProducts[i] = rightRunningProduct
        rightRunningProduct *= array[i]

    for i in range(len(array)):
        products[i] = leftProducts[i] * rightProducts[i]

    return products


def arrayProductsOptimal(array):
    products = [1 for _ in range(len(array))]

    leftRunningProduct = 1
    for i in range(len(array)):
        products[i] = leftRunningProduct
        leftRunningProduct *= array[i]

    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        products[i] *= rightRunningProduct
        rightRunningProduct *= array[i]

    return products

if __name__ == '__main__':
    array = [5, 1, 4, 2]
    print(arrayProductsOptimal(array))
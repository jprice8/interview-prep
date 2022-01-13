def rightSmallerThan(array):
    output = [0 for _ in array]

    for i in range(len(array)):
        smaller = 0
        value = array[i]
        for j in range(i + 1, len(array)):
            rightValue = array[j]
            if rightValue < value:
                smaller += 1
        output[i] = smaller 

    return output


if __name__ == '__main__':
    array = [8, 5, 11, -1, 3, 4, 2]
    print(rightSmallerThan(array))
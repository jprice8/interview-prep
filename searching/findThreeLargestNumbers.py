# O(nlog(n)) time | O(1) space - n is the number elements in the array.
def findThreeLargestNumbers(array):
    output = array[:3]
    output.sort()
    
    if len(array) <= 3:
        return output

    for idx in range(3, len(array)):
        currentNumber = array[idx]
        secondOuput = output[1]
        thirdOutput = output[2]

        # Check for first number
        if currentNumber > output[0]:
            # Check for second number
            if currentNumber > output[1]:
                # Check for third number
                if currentNumber > output[2]:
                    # Swap third output with second and second with first.
                    output[1] = thirdOutput
                    output[0] = secondOuput
                    output[2] =  currentNumber
                else:
                    # Swap second with first.
                    output[0] = secondOuput
                    output[1] = currentNumber
            else:
                output[0] = currentNumber

    return output


# O(n) time | O(1) space
def aeSolution(array):
    threeLargest = [None, None, None]
    for num in array:
        updateLargest(threeLargest, num)
    return threeLargest


def updateLargest(threeLargest, num):
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num, 2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num, 1)
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest, num, 0)


def shiftAndUpdate(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num 
        else:
            array[i] = array[i + 1]


if __name__ == '__main__':
    array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
    print(findThreeLargestNumbers(array))
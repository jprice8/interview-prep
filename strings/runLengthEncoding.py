def runLengthEncoding(string):
    counter = 1
    idx = 1
    results = []

    for idx in range(1, len(string)):
        currentChar = string[idx]
        prevChar = string[idx - 1]

        if currentChar == prevChar and counter < 9:
            counter += 1 
        else:
            # Add to results
            results.append(str(counter))
            results.append(prevChar)
            # Reset counter
            counter = 1

    results.append(str(counter))
    results.append(string[len(string) - 1])

    return ''.join(results)


if __name__ == '__main__':
    string = 'ACCDD'
    print(runLengthEncoding(string))
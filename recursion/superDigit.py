def superDigit(n, k):
    superString = n * k
    return calcSuperString(superString)


def calcSuperString(string):
    if len(string) == 1: return string

    newDigit = 0
    for i in range(len(string)):
        newDigit += int(string[i])

    return calcSuperString(str(newDigit))


if __name__ == '__main__':
    n = '148'
    k = 3
    print(superDigit(n, k)) # 3
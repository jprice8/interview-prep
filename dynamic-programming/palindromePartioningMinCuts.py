def palindromeMinCuts(string):
    if len(string) < 2:
        return 1

    if string == string[::-1]:
        return 1

    cutCount = 0

    for i in range(len(string)):
        prefix = string[:i]
        suffix = string[i:]
        recursiveResult = palindromeMinCuts(prefix) + palindromeMinCuts(suffix)
        cutCount += recursiveResult

    return cutCount


if __name__ == '__main__':
    string = 'ira'
    print(palindromeMinCuts(string))
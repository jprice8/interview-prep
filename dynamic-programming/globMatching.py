from fileinput import filename


def globMatching(fileName, pattern):
    matchTable = initTable(fileName, pattern)

    for i in range(1, len(matchTable) + 1):
        for j in range(1, len(matchTable[i]) + 1):
            if pattern[j - 1] == '*':
                matchTable[i][j] = matchTable[i][j - 1] or matchTable[i][j - 1] or matchTable[i - 1][j]
            elif pattern[j - 1] == "?" or pattern[j - 1] == fileName[i - 1]:
                matchTable[i][j] = matchTable[i - 1][j - 1]
    return matchTable[len(fileName)][len(pattern)]



def initTable(fileName, pattern):
    matchTable = [[False for j in range(len(pattern) + 1)] for i in range(len(fileName) + 1)]

    matchTable[0][0] = True 
    for j in range(1, len(pattern) + 1):
        if pattern[j - 1] == "*":
            matchTable[0][j] = matchTable[0][j - 1]

    return matchTable

if __name__ == '__main__':
    fileName = 'abcdefg'
    pattern = 'a*e?g'
    print(globMatching(fileName, pattern))
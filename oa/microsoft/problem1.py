def solution(A, K):
    n = len(A)
    for i in range(n - 1):
        if (A[i] + 1 < A[i + 1]):
            return False 

    if (A[0] != 1 or A[n - 1] != K):
        return False 
    else:
        return True 

def problem2(S, T):
    def convertString(string):
        res = []
        idx = 0
        while idx < len(string):
            char = string[idx]
            if char.isnumeric():
                numList = []
                while idx < len(string) and string[idx].isnumeric():
                    numList.append(string[idx])
                    idx += 1

                num = int(''.join(numList))
                for _ in range(num):
                    res.append('.')
            else:
                res.append(char)
                idx += 1
        return res

    sList = convertString(S)
    tList = convertString(T)

    # if not same length, can't be same word
    if len(sList) != len(tList):
        return False

    for idx in range(len(sList)):
        sChar = sList[idx]
        tChar = tList[idx]
        # three scenarios
        if sChar == '.':
            continue
        elif tChar == '.':
            continue 
        elif sChar != tChar:
            return False

    return True



# print(problem2('A2Le', '2pL1'))
print(problem2('a10', '10a'))
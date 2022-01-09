# Brute Force
# Time - O(n^m * m) time - where n is length of word bank and m is target. Due to recursive calls and the splice for suffix.
# Space - O(m^2) space - where m is target. Due to m recursive calls on stack and additional m string of suffix.
def countConstruct(target, wordBank):
    if target == '': return 1

    runningCount = 0
    
    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            constructResult = countConstruct(suffix, wordBank)
            runningCount += constructResult

    return runningCount


# Time - O(n * m^2) where n is length of wordbank and m is target.
# Space - O(m^2) where m is target. 
def countConstructMemo(target, wordBank, memo=None):
    if memo is None:
        memo = {}

    if target in memo: return memo[target]
    if target == '': return 1
    
    runningCount = 0

    for word in wordBank:
        if target.find(word) == 0:
        # word is a prefix of target
            suffix = target[len(word):]
            constructResult = countConstructMemo(suffix, wordBank, memo)
            runningCount += constructResult

    memo[target] = runningCount
    return runningCount


if __name__ == '__main__':
    # print(countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) # 1
    # print(countConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) # 0
    # print(countConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) # 4
    # print(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeeee'])) # 0

    print(countConstructMemo('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) # 1
    print(countConstructMemo('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) # 0
    print(countConstructMemo('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) # 4
    print(countConstructMemo('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeeee'])) # 0
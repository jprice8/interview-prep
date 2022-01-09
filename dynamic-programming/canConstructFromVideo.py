def canConstruct(target, wordBank):
    if target == '': return True 

    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            if canConstruct(suffix, wordBank): return True 

    return False

def canConstructMemo(target, wordBank, memo=None):
    if memo is None:
        memo = {}
    if target in memo: return memo[target]
    if target == '': return True 

    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            memo[target] = canConstructMemo(suffix, wordBank, memo)
            if memo[target]: return True

    return False


if __name__ == '__main__':
    # print(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) # True
    # print(canConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) # False
    # print(canConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) # True
    # print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeeee']))

    print(canConstructMemo('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) # True
    print(canConstructMemo('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) # False
    print(canConstructMemo('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) # True
    print(canConstructMemo('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeeee']))
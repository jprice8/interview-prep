def allConstruct(target, wordBank):
    if target == '': return [[]]

    for word in wordBank:
        if target.find(word) == 0:
            prefix = target[len(word):]
            constructResult = allConstruct(prefix, wordBank)
            if constructResult is not None:
                constructResult.append(word)

    return None




if __name__ == '__main__':
    print(allConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
KEYMAP = {
    '0': ['0'],
    '1': ['1'],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

def phoneNumberM(phoneNumber):
    mnemonicsFound = []
    currentMnemonic = [0 for _ in phoneNumber]
    recursiveHelper(0, phoneNumber, mnemonicsFound, currentMnemonic)
    return mnemonicsFound


def recursiveHelper(idx, phoneNumber, mnemonicsFound, currentMnemonic):
    if idx == len(phoneNumber):
        mnemonic = ''.join(currentMnemonic)
        mnemonicsFound.append(mnemonic)
    else:
        digit = phoneNumber[idx]
        letters = KEYMAP[digit]

        for letter in letters:
            currentMnemonic[idx] = letter
            recursiveHelper(idx + 1, phoneNumber, mnemonicsFound, currentMnemonic)


if __name__ == '__main__':
    print(phoneNumberM('1905'))
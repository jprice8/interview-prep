def phoneNumberM(phoneNumber):
    keyMap = {
        '0': '0',
        '1': '1',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    # Loop through all digits in the given phone number.
    for i in range(len(phoneNumber)):
        resultString = ''
        currentDigit = phoneNumber[i] 
        if currentDigit == '0' or currentDigit == '1':
            # Handle 0 and 1
            resultString += keyMap[currentDigit]
        else:
            # Loop through all results in keymap and 
            print('hello')


def recursiveHelper(phoneNumber):
    print('hello')


if __name__ == '__main__':
    print(phoneNumberM('1905'))